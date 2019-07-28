import discord
import json
import os
from discord.ext import commands

#Servers {}

TOKEN = 'NjA0MTg4MDEzMTM5OTg0Mzg0.XT0i9g.TakOhWcCoKy0zPOSKZNinaaZ-d8'

client = commands.Bot(command_prefix = '>>')

@client.event
async def on_ready():
    print('test')
    await client.change.presence(game=discord.Game(name='No Direct Message', type=0))


client.run(TOKEN)
