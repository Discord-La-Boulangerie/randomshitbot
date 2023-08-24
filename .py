#Import des libs python de base
import os, sys
import datetime
import json
import random
from dotenv import load_dotenv
from typing import Optional
from io import BytesIO
import asyncio

#Import de discord et modules discord
import discord 
from discord import app_commands
from discord.ext import tasks
from discord.gateway import DiscordWebSocket, _log
from discord.utils import MISSING, get

#Import des API
import blagues_api as bl
import brawlstats as brst
import enkanetwork as enk
import fortnite_api as ftn
from rule34Py import rule34Py as r34

#paramètres

load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")

# client def
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        await self.tree.sync()
        await self.tree.sync(guild=guild_id1)
intents = discord.Intents.all()
client = MyClient(intents=intents)
guild_id = 1130945537181499542
guild_id1 = discord.Object(id=guild_id)
botlink=f"https://discordapp.com/users/1102573935658283038"

#login check + bot login events
@client.event
async def on_message(message: discord.Message):
    if message.author.bot == False:
        names = ["Adolph Hitler","La bite de Nightye", "Le respect", "Le communisme", "Emmanuel Macron", "Lotus", "Milanozore", "Lotharie", "Jésus", "Un Pokemon sauvage", "Le tartineur de daronnes", "Le FBI", "Eric Zemmour"]
        e = random.choice(names)
        if not message.channel.id ==1131864743502696588:
            if random.randint(1, 50) == 1:
                for guild in client.guilds:
                    await guild.me.edit(nick=e)
                    await asyncio.sleep(10)
                    async with message.channel.typing():
                        await asyncio.sleep(5)
                        await guild.me.edit(nick=None)
                    break
@client.event
async def on_ready():
    print("="*10 + " Build Infos " + "="*10)
    print(f"Connecté en tant que {client.user.display_name} ({client.user.id})") #type: ignore
    print(f"Discord info : {discord.version_info.major}.{discord.version_info.minor}.{discord.version_info.micro} | {discord.version_info.releaselevel}")
    await client.change_presence(status=discord.Status.offline)
client.run(str(DISCORD_TOKEN))