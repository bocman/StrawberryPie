import requests
import re

SEA_TEMPERTURE_LINK = "http://www.seatemperature.org/europe/slovenia/izola.htm"

response = requests.get(url=SEA_TEMPERTURE_LINK)

re_expression = re.match( r'.* <div id="sea-temperature" class="warm">.*', response.text, re.M|re.I)
match = re_expression.group('')
print "-->" + match

print response.text.encode('utf-8')
