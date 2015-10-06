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
from django.views.generic import ListView, CreateView, View, UpdateView
from django.views.generic.edit import FormView
from django.utils import timezone as tz
from django.core.exceptions import ObjectDoesNotExist

import logging
import requests
import json
from dateutil.parser import parse

import project.settings as settings
from forms import ClientForm, ModulForm, EventForm, UserForm, GroupForm
from models import Client, Event, EventActivationElements, ElementGroup, Modul
from rest_services.serializers import *
from .tasks import handle_event
from utils import used_moduls, get_moduls


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


class AddGroupView(FormView, CreateView):
    form_class = GroupForm
    template_name = "settings/groups/add_edit_group.html"
    success_url = "/settings/groups/"


@login_required
def clients_list(request):
    """
    This method is used to get all Clients. At the moment, Clients are
    also sorted by
    status, so Clients which are online are set before those which aren't
    :return: List of Client objects
    """
    template_name = 'settings/clients/clients.html'
    clients = Client.active.all().order_by('disabled')
    return TemplateResponse(request, template_name, {
        'clients': clients,
    })


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


class ModulList(View):
    template_name = "settings/moduls/moduls_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['moduls'] = used_moduls(1)
        names = []
        for name in context['moduls']:
            names.append(name.get('name', None))
        context['modul_names'] = names

        return TemplateResponse(
            request,
            self.template_name,
            context
        )


class ModulCreateView(FormView):
    form_class = ModulForm
    template_name = "settings/moduls/add_edit_modul.html"
    success_url = "/settings/moduls"

    def get(self, *args, **kwargs):
        return TemplateResponse(
            self.request,
            self.template_name, {
                'form': self.form_class
            })

    def post(self, request, *args, **kwargs):
        # Process view when the form gets POSTed
        pass
    form_class = GroupForm
    template_name = "settings/events/add_edit_event.html"
    success_url = "/settings/clients"


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
    msg = {
        'activated': 'Activated modul with pin {0} on client {1}',
        'deactivated': '"Dectivated modul with pin {0} on client {1}',
        'failed': 'Failed to activate modul with pin{0} on client{1}'
    }
    data = {
        "is_activated": status
    }
    client = Client.objects.get(id=client_id)
    url = "http://{0}/rest/gpio/update/{1}/".format(client.ip_address, pin_number)
    try:
        if send_data(url, data) == 200:
            if status == 'True':
                log.info(msg['activated'].format(pin_number, client.name))
            else:
                log.info(msg['deactivated'].format(pin_number, client.name))
    except:
        log.info(msg['failed'].format(pin_number, client.name))

    return HttpResponseRedirect(reverse('settings:clients_list'))


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
        # group_id = self.request.POST.get('act_element', None)
        group_id = None
        modul_id = self.request.POST.get('act_element', None)

        start_task = handle_event.apply_async(eta=start)
        end_task = handle_event.apply_async(eta=end)
        form.instance.start_task_id = start_task.task_id
        form.instance.end_task_id = end_task.task_id
        form.instance.save()

        activation = EventActivationElements()
        activation.event = form.instance
        if group_id:
            activation.group_id = group_id
        if modul_id:
            activation.modul_id = modul_id
        activation.save()
        return super(AddEventView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddEventView, self).get_context_data(**kwargs)
        moduls = used_moduls(1)
        context['moduls'] = moduls if moduls else None
        context['events'] = Event.objects.all()
        return context

    def get_success_url(self):
        return reverse('dashboard:dashboard')


class EditEventView(FormView, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "settings/events/add_edit_event.html"
