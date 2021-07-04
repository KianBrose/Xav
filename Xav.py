import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from discord import *
from discord.utils import get


bot = commands.Bot(command_prefix='€')


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

@client.command(help="jus animenews 1")
async def animenews(message, number):
    import re
    URL = 'https://www.animenewsnetwork.com'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('a', attrs={'href': re.compile('/news/20.+')})[:int(number)]
    for r in results:
        print(r.text)
        print(URL + r['href'])
    await message.channel.send(r.text)
    await message.channel.send(URL + r['href'])

@client.command()
async def hello(message):
    await message.channel.send('Hello!')

@client.command()
async def hi(message):
    await message.channel.send('Hello!')
    
@client.command(help="ask u a ques in english")
async def ask(message): 
    await message.channel.send(random.choice(ques_list))
ques_list=["1. What’s your favorite way to spend a day off?", "What type of music are you into?", "What was the best vacation you ever took and why?", "Where’s the next place on your travel bucket list and why?", "What are your hobbies, and how did you get into them?", "What was your favorite age growing up?", "Was the last thing you read?", "Would you say you’re more of an extrovert or an introvert?", "What's your favorite ice cream topping?", " What was the last TV show you binge-watched?", " Are you into podcasts or do you only listen to music?", " Do you have a favorite holiday? Why or why not?", " If you could only eat one food for the rest of your life, what would it be?", " Do you like going to the movies or prefer watching at home?", " What’s your favorite sleeping position?", " What’s your go-to guilty pleasure?", " In the summer, would you rather go to the beach or go camping?", " What’s your favorite quote from a TV show/movie/book?", " How old were you when you had your first celebrity crush, and who was it?", " What's one thing that can instantly make your day better?", " Do you have any pet peeves?", "what is your favourite anime?", "how many mangas You read?"] 
bot.run("")
