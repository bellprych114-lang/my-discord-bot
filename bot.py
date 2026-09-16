import os
import threading
from flask import Flask
import discord
from discord.ext import commands

# --- ส่วน Web Server หลอก Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    # Render จะส่ง PORT มาทาง Environment Variable (ปกติคือพอร์ต 10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# รัน Web Server แยก Thread เพื่อไม่ให้บล็อกการทำงานของบอท
threading.Thread(target=run_flask, daemon=True).start()

# --- ส่วน Discord Bot ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'บอทออนไลน์แล้วในชื่อ {bot.user}')

@bot.command()
async def ดังโงะซัง(ctx):
        await ctx.send("""🍡 - 「はい～！ ดังโงะ (団子/だんご) เองค่ะ~」 🎀 บอทประจำดิส Strawberry Shortcake 🍰 🍓 คอยดูแลช่วยเหลือ และเติมความน่ารักให้ทุกคนในเซิร์ฟเวอร์ค่ะ ♡ !""")
    
token = os.environ.get('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("ไม่พบ DISCORD_TOKEN ใน Environment Variables")

