# Import Statements
from dotenv import load_dotenv
import json
import os
import requests

# Methods to fetch from Weather API
def currentWeather(location):
    city = location
    country = "Australia"
    place = city + "," + country
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (place, apikey)
    response = requests.get(url)
    print(response.text)
    data = json.loads(response.text)
    returnedCountry = data['sys']['country']
    if returnedCountry != "AU":
        message = location + " in Australia does not exist"
        return message
    else:
        return data

load_dotenv(".env", verbose=True)
apikey = os.getenv('APIKEY')
currentWeather('Sydney')