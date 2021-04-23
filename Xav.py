import discord
from discord.ext import commands, tasks    
import random


bot = commands.Bot(command_prefix='€')

GUILD_ID = 711325947269349448


@tasks.loop(hours=1)
async def change_active_color():
    active_role = bot.get_guild(GUILD_ID).get_role(766278169849364481)

    while True:
        r, g, b = [random.randint(0, 255) for _ in range(3)]

        if (r, g, b) not in list(map(lambda role: role.color.to_rgb(), bot.get_guild(GUILD_ID).roles)):
            break

    await active_role.edit(colour=discord.Colour.from_rgb(r, g, b))


@bot.event()
async def on_ready():
    print(f"Logged as {bot.user}")

    change_active_color.start()


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
    await ctx.send("Welcome!")


bot.run('')

