from celery import task
from project._celery import app
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from datetime import datetime
import requests
import logging
import json

import project.settings as settingsSSS
from .models import Event, EventActivationElements, Modul, Client
from dashboard.models import TemperatureLog
#from views import activate_modul
from core.utils import activation as activate


log = logging.getLogger(__name__)
logger = get_task_logger(__name__)


@task(bind=True)
def handle_event(self):
    logger.info(self.request.id)
    try:
        event = Event.objects.get(start_task_id=self.request.id)
    except:
        try:
            event = Event.objects.get(end_task_id=self.request.id)
        except:
            event = None
    if event:
        activations = EventActivationElements.objects.filter(event=event)
        for activation in activations:
            if activation.modul_id:
                client = Client.objects.get(id=1)
                if not event.is_active:
                    logger.info("READY to ACTIVATE modul")
                    logger.info("MODUL ID is "+ str(activation.modul_id))
                    activate(
                        status=True,
                        client_id=client.id,
                        pin_number=activation.modul_id
                        )
                    event.is_active = True
                else:
                    logger.info("READY to DEACTIVATE modul")
                    activate(
                        status=False,
                        client_id=client.id,
                        pin_number=activation.modul_id
                        )
                    event.is_active = False

            if activation.group:
                if not event.is_active:
                    logger.info("READY to ACTIVATE group")
                else:
                    logger.info("READY to DEACTIVATE group")
    else:
        logger.info("Event does not exist with this arguments")

    event.save()
# A periodic task that will run every minute (the symbol "*" means every)

@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def example():
    print "sem ja"
    logger.info("BOSTJAN NOVAK zacetek")
    logger.info("BOSTJAN END")
    log.info("sem logiral BOSTJAN")



    WEATHER_LOCATION = "Izola"
    WEATHER_API_KEY = "1e408decf36cd52f"
    WEATHER_API_LINK = "http://api.wunderground.com/api/"+ WEATHER_API_KEY+"/conditions/q/CA/"+WEATHER_LOCATION +".json"


    response = requests.get(url=WEATHER_API_LINK)
    data = json.loads(response.text)
    description = data["current_observation"]["icon"]

    a = TemperatureLog()
    a.city = str(data["current_observation"]["display_location"]["city"])
    a.temp = data["current_observation"]["temp_c"]
    a.description = str(data["current_observation"]["icon"])
    a.timestamp =  datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    a.humidity = int(data["current_observation"]["relative_humidity"].replace("%", ""))
    a.wind = data["current_observation"]["wind_kph"]
    a.feels_like = float(data["current_observation"]["feelslike_c"])

    a.save()
