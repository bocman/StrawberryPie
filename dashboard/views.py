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
from dashboard.models import TemperatureLog

log = logging.getLogger(__name__)



def dashboard(request):
    """
    TODO
    """
    weather_data = weather_widget()
    context = {
        'clients_online': Client.online.count(),
        'weather_data': weather_data if weather_data else None,
        'icon': static('weather/Sunny.png')
    }
    #log.info(weather_info(global_settings.WEATHER_API_LINK))
    return TemplateResponse(request, 'dashboard/dashboard.html', context)


def weather_widget(country_name=None):
    """
    TODO
    """
    if TemperatureLog.objects.latest('timestamp'):
        return TemperatureLog.objects.latest('timestamp') 
    else:
        return None

def weather_full(request):
    """
    TODO
    """
    all_weather_info = TemperatureLog.objects.all().order_by('-timestamp')
    return TemplateResponse(request, 'dashboard/weather.html', {
        'data': all_weather_info,
    })






