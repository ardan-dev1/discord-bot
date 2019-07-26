import discord
import json
import os
from discord.ext import commands

#Servers {}

TOKEN = 'NjA0MTg4MDEzMTM5OTg0Mzg0.XTqUYg.ly6epEBn7rBCSwkdrk7j933oAjY'

client = commands.Bot(command_prefix = '>>')

@client.event
async def on_ready():
    print('test')
    await client.change_presence(activity=discord.Streaming(name="SinaKR's Discord | Users {}".format(len(client.guilds), len(client.users)), url="https://www.twitch.tv/ardankjr"))


client.run(TOKEN)
