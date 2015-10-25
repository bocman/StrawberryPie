import requests
from requests.exceptions import ConnectionError
import json

import logging

from .models import Client

log = logging.getLogger(__name__)


def all_online_moduls():
    moduls = []
    online_clients = Client.online.all()
    if online_clients:
        for client in online_clients:
            moduls += client.moduls()
        if moduls:
            return moduls
        else:
            return None
    else:
        return None

