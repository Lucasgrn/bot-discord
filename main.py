import discord
from discord.ext import commands
from lyric import getLyrics
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def lyric(ctx, *, arg):
  
  result = getLyrics(arg)
  if type(result) == list:
    for verse in result:
      await ctx.send(verse)
  else:
    await ctx.send(result)

@bot.command()
async def test(ctx, arg):
  await ctx.send(arg)


bot.run(os.getenv("DISCORD_KEY"))