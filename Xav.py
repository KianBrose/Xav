import discord
from discord.ext import commands



bot = commands.Bot(command_prefix='€')


@bot.event
async def on_ready():
    print(f"Logged as XAV")
    
    
@bot.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("€bye"):
		await message.channel.send("did u actually think i care about your departure? lmao")
	if message.content.startswith("€iq"):
		iq=random.randrange(-1,200)
		await message.channel.send(iq)
		val1, val2, val3 = random.randint(0,9), random.randint(0,9), random.randint(0,9)
		lst1=["u prolly do oc redstone builds dont you",
"damn bro does your brain contribute for 99% of your body weight? prolly not since you use discord you fat piece of shit, go out and see the sun for a while",
"u prolly fap to neil degrasse tyson dont you?",
"woah big brain",
"do u eat books for lunch",
"zombie's delicacy",
"hahah just kidding your iq is in the negatives lol",
"god either gives u a big pp or a big brain, so...",
"do you feel happy that a randomised score given by a discord bot fuels your superiority complex?",
"fun fact, your iq is the same as doras :D",
"how many social interactions have u missed to get this score?"]
		lst2=["average",
"you probably were the gifted kid werent you? look at you now, using a discord bot to validate your superiority complex",
"middle of the pack as always",
"u prolly watch anime and think you are smart for knowing what they said without using the subtitles don't you?",
"your buy books thinking your smart only to not read it becuase u dont understand anything in the book",
"woah, ur so close to glory, yet so far",
"haha noob",
"wow, the perfect iq to work as a walmart cashier",
"i am pretty sure you have a god complex",
"hey nice iq score :), that is if you're autistic"]
		if iq=200:
			await message.channel.send(lst1[val1])
		if iq<150 and iq>=100:
			await message.channel.send(lst2[val2])
		if iq<100:
			await message.channel.send("your iq is so bad that i dont even think its worth my computational power to send a characteristic message to you")

            
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
