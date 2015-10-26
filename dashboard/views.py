from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.templatetags.static import static
from django.utils import timezone as tz
from django.core.exceptions import ObjectDoesNotExist

import requests
import json
import logging
 
import project.settings as global_settings
from setting.models import Client, Modul, Event
from dashboard.models import TemperatureLog

log = logging.getLogger(__name__)


def dashboard(request):
    """
    TODO
    """
    weather_data = weather_widget()
    context = {
        'clients_online': clients_online(),
        'weather_data': weather_data if weather_data else None,
        'icon': static('images/weather/Sunny.png'),
        'event': next_event()
    }
    # log.info(weather_info(global_settings.WEATHER_API_LINK))
    return TemplateResponse(request, 'dashboard/dashboard.html', context)

def clients_online():
    return Client.online.count()

def next_event():
    now = tz.localtime(tz.now())
    try:
        return Event.objects.filter(start_time__gt=now).order_by('start_time')[0]
    except IndexError:
        return None
    except:
        return None

def weather_widget(country_name=None):
    """
    TODO
    """
    try:
        return TemperatureLog.objects.latest('timestamp')
    except:
        return None


def weather_full(request):
    """
    TODO
    """
    weather_data = TemperatureLog.objects.all().order_by('timestamp')
    temperature = []
    feels_like = []
    for counter, item in enumerate(weather_data):
        temperature.append([counter, item.temp])
        feels_like.append([counter, item.feels_like])

    return TemplateResponse(request, 'dashboard/weather.html', {
        'data': weather_data,
        'temperature_data': temperature,
        'feels_like_data': feels_like
        }
    )
