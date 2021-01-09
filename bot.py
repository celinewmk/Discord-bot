import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('Nzk3NTA3MTQ0ODc0MDY1OTIw.X_neaA.jERDBbzeqsoG8AO77Bd6dlnqsYw')
