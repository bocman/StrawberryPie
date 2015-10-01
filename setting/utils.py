import requests
from requests.exceptions import ConnectionError
import json

from .models import Client


def get_moduls(client_id, url=None):
    """
    This method make request on specific client to get all moduls.
    """
    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return None
    if client.port:
        url = "http://{0}:{1}/rest/gpio/all/".format(client.ip_address, client.port)
    else:
        url = "http://{0}/rest/gpio/all/".format(client.ip_address)
    try:
        r = requests.get(url, timeout=3.0)
        moduls = json.loads(r.text)

        for i in moduls:
            group_id = i.get('group', None)
            #i['group'] = ClientGroup.objects.get(id=group_id)
        return moduls
    except ConnectionError as e:
        return None
    except requests.exceptions.Timeout:
        return None

def all_moduls():
    """
    This method return all moduls from all active Clients. This
    mean that we get all free + all used moduls in response.
    """
    clients = Client.objects.all()
    moduls = []
    for client in clients:
        result = get_moduls(client.id)
        if result:
            moduls += result

    return moduls


def free_moduls(client_id):
    """
    This method return all moduls, which are marked as free.
    Modul is marked as free if it is not marked as used. This mean
    that user has not yet created modul with specific pin number.

    TODO
    """
    moduls = []
    for modul in get_moduls(client_id):
        if not modul['is_used']:
            moduls.append(modul)
    if moduls:
        return moduls
    else:
        return None


def used_moduls(client_id):
    """
    This method return all moduls, which are marked as used.
    Modul is marked as used, when user create new one with defined
    pin number on Client. In case that client_id is None, function return
    used moduls from all active Clients, otherway it returns only moduls, which
    are connected on this specific client.

    TODO
    add suport for client_id
    """
    moduls = []
    for modul in get_moduls(client_id):
        if modul['is_used']:
            moduls.append(modul)
    if moduls:
        return moduls
    else:
        return None
