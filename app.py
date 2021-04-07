# Import Statements
import discord
import requests
from dotenv import load_dotenv
import os
import json

# Initialise Client Connection to Discord
client = discord.Client()

def currentWeather(location):
    city = location
    country = "Australia"
    place = city + "," + country
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (place, apikey)
    print(url)
    response = requests.get(url)
    data = json.loads(response.text)
    returnedCountry = data['sys']['country']
    if returnedCountry != "AU":
        message = location + " in Australia does not exist"
        return message
    else:
        return data

# Listen for Discord Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

    if message.content.startswith('$weather'):
        #city = msg.split("$weather ",1)[1]
        if len(msg) > 9:
            city = msg.split("$weather ",1)[1]
            text = currentWeather(city)
            await message.channel.send(text)
        else:
            await message.channel.send("Please enter a valid city in Australia")

    # if message.content.startswith('$country'):
    #     setCountry = msg.split("$country ",1)[1]
    #     updateCountry(setCountry)
    #     await message.channel.send("Weather country has now been set to " + setCountry)

# Load Environmental Variables
load_dotenv(".env", verbose=True)
apikey = os.getenv('APIKEY')
client.run(os.getenv('TOKEN'))
