# Import Statements
from dotenv import load_dotenv
from discord.ext import commands
import os
from weather_api import currentWeather,forecastWeather

# Load Environmental Variables
load_dotenv(".env", verbose=True)
TOKEN = os.getenv('TOKEN')

# Bot Configuration
config = {
    'units': 'degrees'
}

# Initialise Client Connection to Discord
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
# Listen for Discord Events
# TODO catch when no arguments were given
@bot.command(name='weather', help='Type !weather {city} to get the current weather for the city.')
async def current_Weather(ctx,city):
    todaysWeather = currentWeather(city)
    await ctx.send(todaysWeather)

@bot.command(name='forecast', help='Type !forecast {city} to get the 7 day forecast for the city.')
async def forecast_Weather(ctx,city):
    forecastedWeather = forecastWeather(city)
    await ctx.send(forecastedWeather)

@bot.command(name='help')
async def help_help(ctx):
    # #TODO? ignore discord chat message if the author of the message was the bot
    # if message.author == client.user:
    #     return
    response = """
    ```
Weather Service Discord Bot - Help Menu
1. Type !help for this help menu.
2. Type !weather {city} to get the current weather for the city.
3. Type !forecast {city} to get the 7 day forecast for the city.
4. Type !settings to change the bot's settings and preferences.
```
"""
    await ctx.send(response)

@bot.command(name='settings')
async def bot_settings(ctx):
    response = """
Weather Service Discord Bot - Settings
To change these settings please type !setting [value].
To see all values for each setting type !setting all
Settings:
    """
    await ctx.send(response)

@bot.event
async def on_ready():
    print('Ready!')
    channel = bot.get_channel(828964390941753366)
    await channel.send('The weather service bot is online. Please type !help for more a list of all the options.')

bot.run(TOKEN)