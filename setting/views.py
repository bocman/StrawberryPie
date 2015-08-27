from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView
from django.utils import timezone as tz

import logging
import requests
import json
from requests.exceptions import ConnectionError
from dateutil.parser import parse

import project.settings as settings
from forms import ClientForm, ModulForm, EventForm, UserForm
from models import Client, Event, EventActivationElements, ElementGroup, Modul
from rest_services.serializers import *
from .tasks import schedule_event


log = logging.getLogger(__name__)


@login_required
def general_settings(request):
    """
    TODO
    """
    template_name = 'settings/general_settings.html'
    return TemplateResponse(request, template_name, {
    })


def user_logout(request):
    """
    This method is used to logout currently logged user
    :param request: Request, which hold information about user
    :type request: Request object
    :return: HttpRsponseRedirect to login page
    """
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def users_list(request):
    """
    This method is in use to get all active users.
    """
    template_name = 'settings/users/users_list.html'
    users = User.objects.all().filter(is_active=True)
    return TemplateResponse(request, template_name, {
        'users': users,
    })


@login_required
def add_edit_user(request, user_id=None):
    """
    TODO
    """
    template_name = 'settings/users/add_edit_user.html'
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = User()

    if request.POST:
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:dashboard'),
                                        {'messages': messages}
                                        )
    else:
        form = UserForm(instance=user)

    return TemplateResponse(request, template_name, {
        'user_form': form,
        'user_id': user_id
    })


@login_required
def groups_list(request):
    """
    This method is used to get all Groups, which are not marked as deleted
    :return: List of Client objects
    """
    template_name = 'settings/groups/groups.html'
    groups = ElementGroup.objects.all()
    return TemplateResponse(request, template_name, {
        'groups': groups,
    })


@login_required
def clients_list(request):
    """
    This method is used to get all Clients. At the moment, Clients are also sorted by
    status, so Clients which are online are set before those which aren't
    :return: List of Client objects
    """
    template_name = 'settings/clients/clients.html'
    clients = Client.active.all().order_by('disabled')
    return TemplateResponse(request, template_name, {
        'clients': clients,
    })


def get_moduls(client_id, url=None):
    """
    This method make request on client to get list of all moduls.
    """
    client = Client.objects.get(id=client_id)
    if client.port:
        url = "http://{0}:{1}/rest/gpio/all/".format(client.ip_address, client.port)
    else:
        url = "http://{0}/rest/gpio/all/".format(client.ip_address)
    try:
        r = requests.get(url)
        moduls = json.loads(r.text)
        for i in moduls:
            group_id = i.get('group', None)
            #i['group'] = ClientGroup.objects.get(id=group_id)
        return moduls
    except ConnectionError as e:
        return None


def shutdown_client(request, client_id):
    client = Client.objects.get(id=client_id)
    url = "http://{0}:{1}/rest/shutdown/".format(client.ip_address, client.port)
    try:
        r = requests.get(url)
        return HttpResponseRedirect(reverse('settings:clients_list'))
    except ConnectionError as e:
        return None


@login_required
def add_edit_client(request, client_id=None):
    """
    Method is used to create or edit some existing client. When new client is created
    notification email is sended on current logged user email.
    :param client_id: ID of the client, which is edited
    :type client_id: Integer
    """
    template_name = 'settings/clients/add_edit_client.html' 
    from_email = settings.EMAIL_HOST
    to_email = request.user.email
    text = {
            'created_email_body': _("New client has been successfully created on %s. To authorize it \
                                         use this generated key %s ."),
            'created_email_subject': _("New client has been successfully created"),
            'created': _("Client '%s' with id=%s has been created"),
            'created_log': _("Email after creation sended for client '%s' with id=%s"),
            'created_success': _('Additional info were sended on email'),
            'edited': "Client '%s' with id=%s has been edited"
    }

    if client_id:
        client = get_object_or_404(Client, pk=client_id)
    else:
        client = Client()
        client.key = get_random_string(length=32)

    if request.POST:
        client_form = ClientForm(request.POST, instance=client)
        if client_form.is_valid():
            client_form.save()
            if not client_id:
                log.info(text['created'] % (client.name, client.id))
                if from_email and to_email:
                    send_mail(
                        text['created_email_subject'],
                        text['created_email_body'] % (settings.DOMAIN_NAME, client.key),
                        from_email, [to_email]
                        )
                    log.info(text['created_log'] % (client.name, client.id))
            else:
                log.info(text['edited'] % (client.name, client.id))

            messages.add_message(request, messages.SUCCESS, text['created_success'])
            return HttpResponseRedirect(reverse('settings:clients_list'), {'messages': messages})
    else:
        client_form = ClientForm(instance=client)

    return TemplateResponse(request, template_name, {
        'client_form': client_form,
        'client_id': client_id if client_id else None,
        'client': client if client_id else None,
        'moduls': get_moduls(client_id) if client_id else None
    })


@login_required
def delete_client(self, client_id):
    """
    This method is in use to mark some client as deleted. This means that
    this client isn't visible anymore, but informations are still saved in
    the database
    :param client_id: Id of the specific Client
    :type client_id: Integer
    :return: HttpResponseRedirect
    """

    client = get_object_or_404(Client, pk=client_id)
    try:
        client.deleted = True
        client.save()
        log.info("Client {0} has been deleted".format(client.name))
    except:
        pass

    return HttpResponseRedirect(reverse('settings:clients_list'))


class ModulList(ListView):
    queryset = Modul.active.all()
    template_name = "settings/moduls/moduls_list.html"
    context_object_name = 'moduls'

    def get_context_data(self, **kwargs):
        context = super(ModulList, self).get_context_data(**kwargs)
        # names = [name.get('name', None) for name in Item.objects.all().values('name') ]
        names = []
        for name in Modul.objects.all().values('name'):
            names.append(name.get('name', None) )
        context['modul_names'] = names
        return context



def send_data(page_url, data=None, action_type=None):
    """
    TODO
    """
    data = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    request = requests.patch(url=page_url, data=data, headers=headers)
    return request.status_code


def activate_modul(request, status, client_id=None, pin_number=None):
    """
    Function is used to activate specific modul on specific client.
    As parameter we get modul pin number and id of parent client. Then we
    fill those values in prepared url string, to get activation url.
    If activation was successfully we get status code 200 and
    we make note into the logs, otherway we make notes about failed activation
    :param client_id: Id of the client, if modul have a parent
    :param pin_number: GPIO number which is used by modul
    :param status: Value which tell as if we would like to activate
                   or deactivate value (True=activate, False=deactivate)
    :type client_id: Integer
    :type pin_number: Integer
    :type status: Boolean
    """
    data = {
        "is_activated": status
    }
    client = Client.objects.get(id=client_id)
    url = "http://{0}/rest/gpio/update/{1}/".format(client.ip_address, pin_number)
    try:
        if send_data(url, data) == 200:
            if status == 'True':
                log.info("Activated modul with pin {0} on client {1}".format(pin_number, client.name))
            else:
               log.info("Dectivated modul with pin {0} on client {1}".format(pin_number, client.name)) 
    except:
        log.info( "Failed to activate modul with pin{0} on client{1}".format(pin_number, client.name) )

    return HttpResponseRedirect(reverse('settings:clients_list'))


def activate_group(request, moduls):
    pass


@login_required
def delete_modul(self, modul_id):
    """
    This method is in use to mark some modul as deleted. This means that
    this modul isn't visible anymore, but informations are still saved in
    the database
    :param modul_id: Id of the specific Client
    :type modul_id: Integer
    :return: HttpResponseRedirect
    """

    modul = get_object_or_404(Modul, pk=modul_id)
    try:
        modul.is_deleted = True
        modul.save()
    except:
        pass

    return HttpResponseRedirect(reverse('settings:moduls_list'))


@login_required
def edit_client_notification(request, client_id):
    template_name = 'settings/edit_client_notification.html'
    return TemplateResponse(request, template_name, {
        'client_id': client_id
    })


def client_statistics(request, client_id):
    template_name = 'settings/clients/client_statistics.html'
    return TemplateResponse(request, template_name, {
        'client_id': client_id
    })


class AddEventView(FormView, CreateView):
    form_class = EventForm
    template_name = "settings/events/add_edit_event.html"
    success_url = "/settings/clients"

    def form_valid(self, form):
        start = form.cleaned_data['start_time']
        end = form.cleaned_data['end_time']
        group_id = self.request.POST.get('activation_group', None)
        modul_id = self.request.POST.get('activation_modul', None)
        task = schedule_event.apply_async(eta=start)
        form.instance.task_id = task.task_id
        form.instance.save()
        activation = EventActivationElements()
        activation.event = form.instance
        if group_id:
            activation.group_id = group_id
        elif modul_id:
            activation.modul = modul_id
        activation.save()
        return super(AddEventView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddEventView, self).get_context_data(**kwargs)
        context['element_groups'] = ElementGroup.objects.all()
        context['events'] = Event.objects.all()
        return context

    def get_success_url(self):
        return reverse('settings:clients_list')


@login_required
def alarms_list(request, alarm_id=None):

    """
    TODO
    """
    template_name = 'settings/actions/alarms_list.html'
    return TemplateResponse(request, template_name, {
    })
