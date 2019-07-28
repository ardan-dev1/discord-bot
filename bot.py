import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print('bot')
    await client.change_presence(activity=discord.Streaming(name="GameForum | {} Users".format(len(client.users)), url='https://www.twitch.tv/ardankjr'))

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


client.run('NjA0MTg4MDEzMTM5OTg0Mzg0.XT1reg.g2FgaB2LTQP-sqVhfVXBByxTl1Q')
