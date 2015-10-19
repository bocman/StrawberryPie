from celery.decorators import periodic_task
from celery.task.schedules import crontab

from datetime import datetime
import requests
import json

from dashboard.models import TemperatureLog


@periodic_task(run_every=(crontab(hour="*", minute=0, day_of_week="*")))
def weather():

    WEATHER_LOCATION = "Izola"
    WEATHER_API_KEY = "1e408decf36cd52f"
    WEATHER_API_LINK = "http://api.wunderground.com/api/"+ WEATHER_API_KEY+"/conditions/q/CA/"+WEATHER_LOCATION +".json"

    response = requests.get(url=WEATHER_API_LINK)
    data = json.loads(response.text)

    a = TemperatureLog()
    a.city = str(data["current_observation"]["display_location"]["city"])
    a.temp = data["current_observation"]["temp_c"]
    a.description = str(data["current_observation"]["icon"])
    a.timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    a.humidity = int(data["current_observation"]["relative_humidity"].replace("%", ""))
    a.wind = data["current_observation"]["wind_kph"]
    a.feels_like = float(data["current_observation"]["feelslike_c"])
    a.save()
