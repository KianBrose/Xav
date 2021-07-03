from dictFile import countriesDict
import discord
import COVID19Py
import os
from discord.ext import commands
client=commands.Bot(command_prefix='%')
@client.event
async def on_ready():
    print('Bot is ready')
@client.command()
async def covidStats(contex, countryName):
    covid19 = COVID19Py.COVID19() 
    country=countriesDict[countryName]
    try:
        cases1 = covid19.getLocationByCountryCode(country)
        cases=str(cases1[0]['latest']['confirmed'])
        string="Number of cases in "+ countryName+ " is: "+ cases
        await contex.send(string)
    except:
        await contex.send("wrong ID")
client.run('Pwut wour cwode hwere UwU')
