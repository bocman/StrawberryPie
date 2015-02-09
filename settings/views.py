from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse


from forms import ClientForm
from models import Client


def clients_list(request):

    clients = Client.active.all()

    return TemplateResponse(request, 'settings/clients.html', {
        'clients': clients
        })


def add_edit_client(request, client_id=None):
    """ """

    if client_id:
        client = get_object_or_404(Client, pk=client_id)
    else:
        client = Client()

    if request.POST:
        client_form = ClientForm(request.POST, instance=client)
        if client_form.is_valid():
            client_form.save()
            return HttpResponseRedirect(reverse('settings:clients_list'))  
    else:
        client_form = ClientForm(instance=client)

    return TemplateResponse(request, 'settings/add_edit.html', {
        'client_form': client_form,
        'client_id': client_id if client_id else None
        })

def delete_client(self, client_id):
    """
    """

    client = get_object_or_404(Client, pk=client_id)
    try:
        client.deleted = True
    except:
        pass


