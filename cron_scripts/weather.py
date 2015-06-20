#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys
import requests
import json
import datetime
 
try:
    con = _mysql.connect('localhost', 'root', 'bostjanNovak1', 'project')
        
    #con.query("INSERT INTO temperature_log (temp) VALUES ('1')")
    #result = con.use_result()
    WEATHER_LOCATION = "Izola"
    WEATHER_API_KEY = "1e408decf36cd52f"
    WEATHER_API_LINK = "http://api.wunderground.com/api/"+ WEATHER_API_KEY+"/conditions/q/CA/"+WEATHER_LOCATION +".json"


    response = requests.get(url=WEATHER_API_LINK)
    data = json.loads(response.text)
    description = data["current_observation"]["icon"]

    context_data = {
        'city': "'" + str(data["current_observation"]["display_location"]["city"]) +"'",
        'temp': data["current_observation"]["temp_c"],
        'description': "'" + str(data["current_observation"]["icon"])+"'",
        'timestamp': "'" + datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")+ "'",
        'humidity': int(data["current_observation"]["relative_humidity"].replace("%", "")),
        'wind': data["current_observation"]["wind_kph"],
        'feels_like': float(data["current_observation"]["feelslike_c"]),
    }
    columns_string= '('+','.join(context_data.keys())+')'    
    values_string = '('+','.join(map(str,context_data.values()))+')'

    con.query( "INSERT INTO temperature_log "+ columns_string +" VALUES "+ values_string )
    result = con.use_result()

except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    
    if con:
        con.close()