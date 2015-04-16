from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages

import logging
from rest_framework import viewsets

from forms import ClientForm
from models import Client
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
    TODO
    """

    if client_id:
        client = get_object_or_404(Client, pk=client_id)
    else:
        client = Client()

    if request.POST:
        client_form = ClientForm(request.POST, instance=client)
        if client_form.is_valid():
            client_form.save()
            messages.add_message(request, messages.SUCCESS, 'Hello world.')
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

class ClientViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = Client.objects.all()
   # serializer_class = ClientSerializer
