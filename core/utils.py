from collections import OrderedDict

from settings.models import Client


def dashboard_data():
    data = OrderedDict()

    data['clients_online'] = Client.objects.count()

    return data
