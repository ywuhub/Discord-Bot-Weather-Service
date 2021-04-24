# Import Statements
from discord.ext import commands
import os
from weather_api import currentWeather,forecastWeather
from keep_alive import keep_alive

# Load Environmental Variables
TOKEN = os.environ['TOKEN']

# Initialise Client Connection to Discord
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

# Listen for Discord Events
@bot.command(name='weather', help='Type !weather {city} to get the current weather for the city.')
async def current_Weather(ctx,*args):
    todaysWeather = currentWeather(args)
    await ctx.send(todaysWeather)

@bot.command(name='forecast', help='Type !forecast {city} to get the 7 day forecast for the city.')
async def forecast_Weather(ctx,*args):
    forecastedWeather = forecastWeather(args)
    await ctx.send(forecastedWeather)

@bot.command(name='help', help='Type !help for a list of all the bot\'s options.')
async def help_help(ctx):
    response = """
```
Weather Service Discord Bot - Help Menu
1. Type !help for this help menu.
2. Type !weather {city} to get the current weather for the city.
3. Type !forecast {city} to get the 7 day forecast for the city.
```
"""
    await ctx.send(response)

@bot.event
async def on_ready():
    print('The Weather Service Bot is running!')
    channel = bot.get_channel(834401398015787012)
    await channel.send('The weather service bot is online. Please type !help for more a list of all the options.')

keep_alive()
bot.run(TOKEN)
