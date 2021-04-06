# Import Statements
import discord
from dotenv import load_dotenv
import os

# Initialise Client Connection to Discord
client = discord.Client()

# Listen for Discord Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

# Load Environmental Variables
load_dotenv(".env", verbose=True)
client.run(os.getenv('TOKEN'))
