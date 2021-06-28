import discord
from discord.ext import commands
import random

from utils import Guild_utils



GUILD_ID = 711325947269349448

bot = commands.Bot(command_prefix='€')
guild = Guild_utils(bot, GUILD_ID)


@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")


@bot.command()
async def info(ctx):
    texttosend = """
    -Ask SPECIFIC questions, don't expect help if you say "It doesn't work" "Why isn't it working" "can you fix it for me" Instead, describe the problem/s, the steps you tried to fix it, the objective etc, don't make people dig infornation out of you
                 """
    await ctx.send(texttosend)


@bot.command()
async def tos(ctx):
    texttosend = """
    - As much as I don't like discord TOS, discussion of cheating or automation of games is not allowed
                 """
    await ctx.send(texttosend)


@bot.command()
async def w(ctx):
    await ctx.send(random.choices(['Welcome', 'Welcum'], [0.99, 0.01]))  # 1% chance of saying "Welcum"


bot.run()
