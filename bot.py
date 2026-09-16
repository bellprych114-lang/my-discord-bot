import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'บอทออนไลน์แล้วในชื่อ {bot.user}')

@bot.command()
async def ดังโงะ(ctx):
    await ctx.send('คะ?!')

bot.run(os.environ.get('DISCORD_TOKEN'))
