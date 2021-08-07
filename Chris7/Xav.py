from discord.ext import commands

from ghost_ping_detector import GhostPingDetector

bot = commands.Bot(command_prefix='€', case_insensitive=True)

bot.add_cog(GhostPingDetector())


@bot.event
async def on_ready():
    print(f"Logged as XAV")


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
    await ctx.send('Welcome')


bot.run("")
