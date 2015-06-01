from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext as _

import logging
from rest_framework import viewsets
import project.settings as settings

from forms import ClientForm, AlarmForm, UserForm
from models import Client, Alarm
#from serializers import ClientSerializer


log = logging.getLogger(__name__)

@login_required
def general_settings(request):   
   
    """
    TODO
    """
    return TemplateResponse(request, 'settings/general_settings.html', {
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
    users = User.objects.all().filter(is_active=True)
    return TemplateResponse(request, 'settings/users_list.html', {
        'users': users,
    })

@login_required
def add_edit_user(request, user_id=None):    
    
    """ 
    TODO
    """
    if user_id:
       user = get_object_or_404(User, pk=user_id)     
    else:
        user = User()

    if request.POST:
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            #messages.add_message(request, messages.SUCCESS, 'Hello world.')
            return HttpResponseRedirect(reverse('dashboard:dashboard'), {'messages':messages})
    else:
        form = UserForm(instance=user)

    return TemplateResponse(request, 'settings/add_edit_user.html', {
        'user_form': form,
        'user_id':user_id
    })

@login_required
def clients_list(request):   
   
    """
    This method is used to get all Clients. At the moment, Clients are also sorted by
    status, so Clients which are online are set before those which aren't
    :return: List of Client objects
    """
    clients = Client.active.all().order_by('disabled')
    return TemplateResponse(request, 'settings/clients.html', {
        'clients': clients,
    })

@login_required
def add_edit_client(request, client_id=None):    
    
    """ 
    Method is used to create or edit some existing client.
    """

    from_email = settings.EMAIL_HOST
    to_email = request.user.email
    text = {'client_created_email': _("New client has been successfully created on %s. To authorize it \
                                         use this generated key %s ."),
                'client_email_subject': _("New client has been successfully created"),
                'client_created': _("Client '%s' with id=%s has been created"),
                'client_edited': "Client '%s' with id=%s has been edited",
                'client_created_log': _("Email after creation sended for client '%s' with id=%s")
               }

    if client_id:
        client = get_object_or_404(Client, pk=client_id)
    else:
        client = Client()
        client.client_key = get_random_string(length=32)

    if request.POST:
        client_form = ClientForm(request.POST, instance=client)
        if client_form.is_valid():
            client_form.save()
            if not client_id:
                log.info(text['client_created'] % (client.name, client.id))
                if from_email and to_email:
                    send_mail(text['client_email_subject'],
                              text['client_created_email'] % (settings.DOMAIN_NAME, client.client_key),
                              from_email, [to_email])
                    log.info(text['client_created_log'] % (client.name, client.id))
            else:
                log.info(text['client_edited'] % (client.name, client.id))
            
            messages.add_message(request, messages.SUCCESS, _('Additional info were sended on email'))
            return HttpResponseRedirect(reverse('settings:clients_list'), {'messages':messages})
    else:
        client_form = ClientForm(instance=client)

    return TemplateResponse(request, 'settings/add_edit_client.html', {
        'client_form': client_form,
        'client_id': client_id if client_id else None,
        'client':client
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

@login_required
def edit_client_notification(request, client_id):
    return TemplateResponse(request, 'settings/edit_client_notification.html', {
        'client_id':client_id
    })

def client_statistics(request, client_id):
    return TemplateResponse(request, 'settings/client_statistics.html', {
    'client_id':client_id
})

@login_required
def add_edit_alarm(request, alarm_id=None):    
    
    """ 
    TODO
    """
    if alarm_id:
        alarm = get_object_or_404(Alarm, pk=alarm_id)
    else:
        alarm = Alarm()
        alarm.client_id = request.GET["client_id"]

    if request.POST:
        alarm_form = AlarmForm(request.POST, instance=alarm)
        if alarm_form.is_valid():
            alarm_form.save()
            if alarm_id:
                log.info("Alarm with id "+str(alarm_id)+" has been edited")
            else:
                log.info("New alarm has been successfully created with")

            return HttpResponseRedirect(reverse('settings:clients_list'))
    else:
        alarm_form = AlarmForm()
    
    return TemplateResponse(request, 'settings/alarm/add_edit_alarm.html', {
        'alarm_form': alarm_form,
        'alarms': Alarm.objects.filter(client_id=1)
    })

@login_required
def alarms_list(request, alarm_id=None):   
   
    """
    TODO
    """    
    return TemplateResponse(request, 'settings/alarms_list.html', {
    })

class ClientViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = Client.objects.all()
   # serializer_class = ClientSerializer
