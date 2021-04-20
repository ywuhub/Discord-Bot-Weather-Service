# Import Statements
from dotenv import load_dotenv
import json
import os
import requests
import datetime
#TODO see if ([a-zA-Z\s])+ regex is neccessary

# Methods to fetch from Weather API

# Adds suffix to date
def ending(day):
    return 'th' if 11<=day<=13 else {1:'st',2:'nd',3:'rd'}.get(day%10, 'th')

# Turns weather into emoji on discord
# TODO Mist,Smoke,Haze,Dust,Sand,Ash,Squall
def emojify(weather):
    if weather == "Clouds":
        return ":cloud:"
    elif weather == "Clear":
        return ":sunny:"
    elif weather == "Rain":
        return ":cloud_rain:"
    elif weather == "Snow":
        return ":cloud_snow:"
    elif weather == "Thunderstorm":
        return ":thunder_cloud_rain:"
    elif weather == "Tornado":
        return ":cloud_tornado:"
    elif weather == "Fog":
        return ":fog:"
    else:
        weathers == ":" + weather + ":"
        return weathers

# Get Longitute and Latitute for the city to get daily forecast from API
def getLatandLong(location):
    country = "Australia"
    place = location + "," + country
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (place, apikey)
        response = requests.get(url)
        data = json.loads(response.text)
        returnedCountry = data['sys']['country']
    except:
        return "Please enter a valid city in Australia"
    if returnedCountry != "AU":
        message = "The city " + location + " does not exist in Australia."
        return message
    else:
        co = []
        co.append(data['coord']['lon'])
        co.append(data['coord']['lat'])
        return co

# Get the current weather for an Australia city
def currentWeather(location):
    city = ' '.join(location)
    country = "Australia"
    place = city + "," + country
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (place, apikey)
        response = requests.get(url)
        data = json.loads(response.text)
        returnedCountry = data['sys']['country']
    except:
        return "Please enter a valid city in Australia"

    if returnedCountry != "AU":
        message = location + " in Australia does not exist"
        return message
    else:
        date = datetime.datetime.now()
        suffix = ending(int(date.strftime("%d")))
        String = date.strftime("%A") + " the " + date.strftime("%d") + suffix + " Weather Conditions are "
        temp = " Min " + str(data['main']['temp_min']) + "°C Max " + str(data['main']['temp_max']) + "°C "
        weather = emojify(data['weather'][0]['main'])
        String = String + temp + "with the skies being " + weather + " " + data['weather'][0]['main']
        return String

# Get the 7 day forecast for an Australia city (TODO: Min info, Standard, Max info)
def forecastWeather(location):
    # find lat and long through current weather
    location = ' '.join(location)
    co = getLatandLong(location)
    if type(co) is str:
        return co
    else:
        lat = str(co[1])
        long = str(co[0])
        try:
            url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=current,minutely,hourly,alerts&appid=%s&units=metric" % (lat,long,apikey)
            response = requests.get(url)
            data = json.loads(response.text)
        except:
            return "Please enter a valid city in Australia"

        String = "Weekly forecast for " + location + "\n"
        date = datetime.datetime.now()
        suffix = ending(int(date.strftime("%d")))
        delta = datetime.timedelta(days=1)
        #array.append("Weekly forecast for " + city)
        for i in data['daily']:
            String = String + date.strftime("%A") + " the " + date.strftime("%d") + suffix + " Weather Conditions are "
            temp = "Min " + str(i['temp']['min']) + "°C Max " + str(i['temp']['max']) + "°C"
            weather = emojify(i['weather'][0]['main'])
            String = String + temp + " with the skies being " + weather + " " + i['weather'][0]['main'] + "\n"
            date += delta
            suffix = ending(int(date.strftime("%d")))
        return String

load_dotenv(".env", verbose=True)
apikey = os.getenv('APIKEY')
