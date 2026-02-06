import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# -------- Flask App --------
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Discord Bot is Running!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

# -------- Discord Bot --------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")

@bot.command()
async def ho(ctx):
    await ctx.send("hello!")

def run_bot():
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)

# -------- Main --------
if __name__ == "__main__":
    Thread(target=run_web).start()
    run_bot()
