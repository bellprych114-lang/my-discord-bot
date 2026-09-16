import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'บอทออนไลน์แล้วในชื่อ {bot.user}')

@bot.command()
async def หวัดดีดังโงะ!(ctx):
    await ctx.send('สวัสดีค่ะ!!')

bot.run('MTU0OTc1NDM4NTYxNjIwNzkxMw.G5IeqZ.i1zy7eSeUVf1hWNubQ15dlO19PfauYDpoaHZns')
