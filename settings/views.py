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
from django.views.generic import ListView

import logging
import requests
import json
from rest_services.serializers import *
import project.settings as settings

from forms import ClientForm, ItemForm, AlarmForm, UserForm
from models import Client, Alarm, ClientGroup, Item
# from serializers import ClientSerializer


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
            # messages.add_message(request, messages.SUCCESS, 'Hello world.')
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
    groups = ClientGroup.objects.all()
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


def get_items(client_id, url=None):
    """
    This method make request on client to get list of all items.
    """
    if not url:
        url = "http://192.168.1.130:8002/rest/gpio/all/"
    r = requests.get(url)
    items = json.loads(r.text)
    for i in items:
        group_id = i.get('group', None)
        #i['group'] = ClientGroup.objects.get(id=group_id)
    return items


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
                    send_mail(text['created_email_subject'],
                              text['created_email_body'] % (settings.DOMAIN_NAME, client.key),
                              from_email, [to_email])
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
        'items': get_items(client_id) if client_id else None
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
    except:
        pass

    return HttpResponseRedirect(reverse('settings:clients_list'))


class ItemsList(ListView):
    queryset = Item.active.all()
    template_name = "settings/items/items_list.html"
    context_object_name = 'items'


def send_data(page_url, data=None, action_type=None):
    """
    TODO
    """
    data = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    result = requests.patch(url=page_url, data=data, headers=headers)

def activate_item(request, pin_number=None, status=None):
    data ={
        'is_activated': status
    }
    page_url= "http://192.168.1.130:8002/rest/gpio/update/"+ str(pin_number)+ "/"
    try:
        send_data(page_url, data)
    except:
        print "i Failed with activation"
        pass
    return HttpResponseRedirect(reverse('settings:clients_list'))


@login_required
def delete_item(self, item_id):
    """
    This method is in use to mark some item as deleted. This means that
    this item isn't visible anymore, but informations are still saved in
    the database
    :param item_id: Id of the specific Client
    :type item_id: Integer
    :return: HttpResponseRedirect
    """

    item = get_object_or_404(Item, pk=item_id)
    try:
        item.is_deleted = True
        item.save()
    except:
        pass

    return HttpResponseRedirect(reverse('settings:items_list'))



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


@login_required
def add_edit_alarm(request, alarm_id=None):

    """
    TODO
    """
    template_name = 'settings/actions/add_edit_alarm.html'
    if alarm_id:
        alarm = get_object_or_404(Alarm, pk=alarm_id)
    else:
        alarm = Alarm()
        alarm.client_id = request.GET.get("client_id", None)
        alarm.group_id = request.POST.get("selected_group", None)
    
    if request.POST:
        alarm_form = AlarmForm(request.POST, instance=alarm)
        log.info("sem 1")
        if alarm_form.is_valid():
            log.info("sem 2")
            alarm_form.save()
            if alarm_id:
                log.info("Alarm with id "+str(alarm_id)+" has been edited")
            else:
                log.info("New alarm has been successfully created with")

            return HttpResponseRedirect(reverse('settings:clients_list'))
    else:
        alarm_form = AlarmForm()

    return TemplateResponse(request, template_name, {
        'action_form': alarm_form,
        'actions': Alarm.objects.all().order_by('start_time'),
        'groups': ClientGroup.objects.all()
    })


@login_required
def alarms_list(request, alarm_id=None):

    """
    TODO
    """
    template_name = 'settings/actions/alarms_list.html'
    return TemplateResponse(request, template_name, {
    })
