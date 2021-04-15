# Import Statements
import discord
from dotenv import load_dotenv
import os
from process_commands import get_current_weather, help_menu, get_forecast_weather

# Initialise Client Connection to Discord
client = discord.Client()

# Listen for Discord Events
@client.event
async def on_message(message):
    # ignore discord chat message if the author of the message was the bot
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$weather'):
        await get_current_weather(msg, message)
    elif message.content.startswith('$forecast'):
        await get_forecast_weather(msg,message)
    elif message.content.startswith('$help'):
        await help_menu(message)

@client.event
async def on_ready():
   channel = client.get_channel(828964390941753366)
   await channel.send("The weather service bot is online. Please type $help for more a list of all the options.")

# Load Environmental Variables
load_dotenv(".env", verbose=True)
client.run(os.getenv('TOKEN'))
