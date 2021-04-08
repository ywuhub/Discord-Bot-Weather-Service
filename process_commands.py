# Import Statements
from weather_api import currentWeather

# Bot Methods
async def get_current_weather(msg, message):
    if len(msg) > 9:
            city = msg.split("$weather ",1)[1]
            text = currentWeather(city)
            await message.channel.send(text)
    else:
        await message.channel.send("Please enter a valid city in Australia")

async def help_menu(message):
    help_text = """
    ```
Weather Service Discord Bot - Help Menu

1. Type !help for this help menu.
2. Type !weather {city} to get the current weather for the city.
3. Type !forecast {city} to get the 7 day forecast for the city.
4. Type !settings to change the bot's settings and preferences.
```
"""
    await message.channel.send(help_text)