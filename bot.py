import discord
import json
import os
from discord.ext import commands

#Servers {}

TOKEN = 'NTQzNDI4OTk5NDE4ODcxODI4.XTsK1A.ilHmxmX_BSpZ4w92SatJFMqI3XI'

client = commands.Bot(command_prefix = '>>')

@client.event
async def on_ready():
    print('test')
    await client.change.presence(game=discord.Game(name='No Direct Message', type=0))


client.run(TOKEN)
