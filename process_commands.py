# Import Statements
from weather_api import currentWeather,forecastWeather

# Bot Methods
async def get_current_weather(msg, message):
    if len(msg) > 9:
        city = msg.split("$weather ",1)[1]
        text = currentWeather(city)
        await message.channel.send(text)
    else:
        await message.channel.send("Please enter a valid city in Australia")

async def get_forecast_weather(msg,message):
    if len(msg) > 9: # find a better way to do this
        city = msg.split("$forecast ",1)[1]
        text = forecastWeather(city)
        await message.channel.send(text)
    else:
        await message.channel.send("Please enter a valid city in Australia")
