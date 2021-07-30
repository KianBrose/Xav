import discord
from discord.ext import commands
import random
import os

import db
from utils import Guild_utils

#cogs
from pool import Pool
from karma import Karma
from giveway import Giveway
from rolereact import RoleReact



GUILD_ID = 711325947269349448
PREFIX = '€'
intents = discord.Intents(messages=True, guilds=True, reactions=True)

bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command('help')

guild = Guild_utils(bot, GUILD_ID)
db.init()

bot.add_cog(Karma(bot))
bot.add_cog(Pool(bot))
bot.add_cog(RoleReact(bot, guild))
bot.add_cog(Giveway(bot, guild))


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
    await ctx.send(random.choices(['Welcome', 'Welcum'], [0.99, 0.01])[0])  # 1% chance of saying "Welcum"


@bot.command()
async def money(ctx):
    await ctx.send(f"{guild.EMOJIS['pepeEvil']} https://www.youtube.com/watch?v=KigVdcSr8s4")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commands available", color=0x34a1eb)

    embed.add_field(name=f"{PREFIX}info", value="display the info message")
    embed.add_field(name=f"{PREFIX}tos", value="display the tos message")
    embed.add_field(name=f"{PREFIX}w", value="display the welc~~um~~ome message")
    embed.add_field(name=f"{PREFIX}money", value="CAPITALISM")
    embed.add_field(name=f"{PREFIX}karma", value="check your current karma")
    embed.add_field(name=f"{PREFIX}pool <question>", value="create a pool")
    embed.add_field(name=f"{PREFIX}rolereact <message link> <emojis> <roles>", value="create a role react event (admin only)")
    embed.add_field(name=f"{PREFIX}giveway <time (d|h|m|s> <prize> <optionnal text>", value="create giveway (admin only)")
    embed.add_field(name=f"{PREFIX}reroll <msglink>", value="reroll the result of a giveway (admin only)")

    await ctx.send(embed=embed)


bot.run(os.environ["TOKEN"])
