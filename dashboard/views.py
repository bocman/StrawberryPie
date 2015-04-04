from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
import requests
import json

import logging
from django.templatetags.static import static
import project.settings as global_settings
from settings.models import Client


log = logging.getLogger(__name__)


def dashboard(request):
    """
    TODO
    """

    context = {
        'clients_online': Client.online.count(),
        'weather_data': weather_info(global_settings.WEATHER_API_LINK)
    }
    #log.info(weather_info(global_settings.WEATHER_API_LINK))
    return TemplateResponse(request, 'dashboard/dashboard.html', context)


def weather_info(country_name):
    """
    TODO
    """
    response = requests.get(url=global_settings.WEATHER_API_LINK)
    data = json.loads(response.text)
    context_data = {
        'city': data["current_observation"]["display_location"]["city"],
        'last_updated': data["current_observation"]["observation_time"],
        'temp': data["current_observation"]["temp_c"],
        'description': data["current_observation"]["icon"],
        'icon': static("weather/Cloudy.png")

    }
    return context_data








