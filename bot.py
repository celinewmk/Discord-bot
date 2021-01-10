import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.',intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


client.run('Nzk3NTE3NDQ3ODQ5NzA1NDgy.X_noAA.sYfzP1j3xjGwHct9mN9D8LrvSRc')
