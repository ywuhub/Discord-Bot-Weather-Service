# Import Statements
from dotenv import load_dotenv
import json
import os
import requests

# Methods to fetch from Weather API

# Get Longitute and Latitute for the city to get daily forecast from API
def getLatandLong(location):
    country = "Australia"
    place = location + "," + country
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (place, apikey)
    response = requests.get(url)
    data = json.loads(response.text)
    returnedCountry = data['sys']['country']
    if returnedCountry != "AU":
        message = location + " in Australia does not exist"
        return message
    else:
        co = []
        co.append(data['coord']['lon'])
        co.append(data['coord']['lat'])
        return co

# Get the current weather for an Australia city
def currentWeather(location):
    city = location
    country = "Australia"
    place = city + "," + country
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (place, apikey)
    response = requests.get(url)
    data = json.loads(response.text)
    returnedCountry = data['sys']['country']
    if returnedCountry != "AU":
        message = location + " in Australia does not exist"
        return message
    else:
        return data

# Get the 5 day forecast (3 hour intervals) for an Australia city
# def fiveDayWeather(location):
#     city = location
#     country = "Australia"
#     place = city + "," + country
#     url = "https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=metric" % (place, apikey)
#     response = requests.get(url)
#     data = json.loads(response.text)
#     returnedCountry = data['sys']['country']
#     if returnedCountry != "AU":
#         message = location + " in Australia does not exist"
#         return message
#     else:
#         return data

# Get the 7 day forecast for an Australia city (TODO: Min info, Standard, Max info)
def forecastWeather(location):
    # find lat and long through current weather
    co = getLatandLong(location)
    if type(co) is str:
        return co
    else:
        lat = str(co[1])
        long = str(co[0])
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=current,minutely,hourly,alerts&appid=%s&units=metric" % (lat,long,apikey)
        response = requests.get(url)
        data = json.loads(response.text)
        String = "Weekly forecast for " + location + "\n"
        #array.append("Weekly forecast for " + city)
        for i in data['daily']:
            temp = "Min " + str(i['temp']['min']) + " Max " + str(i['temp']['max'])
            weather = i['weather'][0]['main']
            String = String + temp + " Weather Condition is " + weather + "\n"
        return String

load_dotenv(".env", verbose=True)
apikey = os.getenv('APIKEY')
