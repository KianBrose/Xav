import discord
from discord_components import *
from discord.ext import commands
from asyncio import TimeoutError
from random import choice

bot = commands.Bot(command_prefix = "!")

ch1 = ["Rock","Scissors","Paper"]


@bot.event 
async def on_ready():
    DiscordComponents(bot)
    print(f"logged in as {bot.user}!")


@bot.command()
async def rps(ctx):

    comp = choice(ch1)
    yet = discord.Embed(title=f"{ctx.author.display_name}'s, Rock Paper Sissors Game!!!", description=f"Status: u haven't clicked on any button yet!",color=0xFFEA00)
    win = discord.Embed(title=f"{ctx.author.display_name}, Impressive u won!", description=f"Status: **u wonn!!!!** Bot has chosen {comp}",color=0xFFEA00)
    out = discord.Embed(title=f"{ctx.author.display_name}, u didn't click on time dummy", description=f"Status: **Timeout!!!**",color=discord.Color.red())
    lost = discord.Embed(title=f"{ctx.author.display_name}, YOU LOST L!!", description=f"Status: **imagine losing to a bot :P** Bot has picked {comp}.",color=discord.Color.red())
    tie = discord.Embed(title=f"{ctx.author.display_name}, woah u scored a tie!!", description=f"Status: **TIE!** Bot has chosen {comp}",color=0xFFEA00)





    m = await ctx.send(
        embed=yet,
        components=[[Button(style=1, label="Rock"),Button(style=3, label="Paper"),Button(style=ButtonStyle.red, label="Scissors")]
        ])

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
        res = await bot.wait_for("button_click", check=check, timeout=15)
        player = res.component.label

        if player==comp:
          await m.edit(embed=tie,components=[])
          
        if player=="Rock" and comp=="Paper":
          await m.edit(embed=lost,components=[])
          
        if player!="Rock" and comp=="Scissors":
          await m.edit(embed=win,components=[])
                
        if player=="Paper" and comp=="Rock":
          await m.edit(embed=win,components=[])
          
        if player=="Paper" and comp=="Scissors":
          await m.edit(embed=lost,components=[])          
          
        if player=="Scissors" and comp!="Rock":
          await m.edit(embed=lost,components=[])
          
        if player=="Scissors" and comp=="Paper":
          await m.edit(embed=win,components=[])
        

    except TimeoutError:
        await m.edit(
            embed=out,
            components=[],
        )       
