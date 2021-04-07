# Import Statements
import discord
from dotenv import load_dotenv
import os
from process_messages import get_current_weather

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

# Load Environmental Variables
load_dotenv(".env", verbose=True)
client.run(os.getenv('TOKEN'))
