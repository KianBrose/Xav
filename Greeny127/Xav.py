import discord
from discord.ext import commands
import random
import ThankYou


bot = commands.Bot(command_prefix='€')

scorebot = ThankYou.ScoreBot("Scores.db", "ScoresTable")
msgbot = ThankYou.MessageKeeperBot("Messages.db", "MessagesTable")


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
    await ctx.send(random.choices(['Welcome', 'Welcum'], [0.99, 0.01]))


@bot.command()
@commands.has_permissions(administrator=True)
async def addScore(ctx, name, score):
    try:    
        scorebot.updateScore(name, int(score))

        await ctx.send("Done!")
    
    except Exception as e:
        await ctx.send(f"Something went wrong - `{e}`")


@bot.command()
@commands.has_permissions(administrator=True)
async def subScore(ctx, name, score):
    try:
        score = int("-" + str(score))
        scorebot.updateScore(name, score)

        await ctx.send("Done!")
    
    except Exception as e:
        await ctx.send(f"Something went wrong - `{e}`")


@bot.command()
async def getPlayer(ctx, name: discord.User):
    newname = str(name.id)
    name = name.name
    try:
        user = scorebot.getData(newname, mode="individual")

        embed = discord.Embed(title="{}'s Score".format(name), description="What's {}'s score?".format(name), color = 0xFF5733)
        embed.add_field(name="Score", value="{} has {} points. Good Job! I guess...".format(name, user[0][1]))
        
        await ctx.send(embed=embed)

    except IndexError:
        await ctx.send("Are you sure that user exists?")
        

@bot.command()
async def thankyou(ctx):
    if ctx.message.reference:
        msg = await ctx.fetch_message(id=ctx.message.reference.message_id)
        try:
            if str(ctx.message.author.id) in msgbot.getMessage(str(msg.id), str(msg.channel.id))[0][2]:
                await ctx.send("You already gave your thanks.")

        except IndexError:
            msgbot.addUser(str(msg.id), str(msg.channel.id), str(ctx.message.author.id))
            scorebot.updateScore(str(msg.author.id), 5)
            scorebot.updateScore(str(ctx.message.author.id), 1)

            await ctx.send("You've sent your thanks. (psst, you got a point as well)")
        
    else:
        await ctx.send("You have to use this as a reply to a message.")


bot.run("")