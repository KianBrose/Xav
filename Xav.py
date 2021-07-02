import discord
from discord.ext import commands
import random
import ThankYou

from utils import Guild_utils

GUILD_ID = 711325947269349448

bot = commands.Bot(command_prefix='€')

guild = Guild_utils(bot, GUILD_ID)
scorebot = ThankYou.ScoreBot("Scores.db", "ScoresTable")
msgbot = ThankYou.MessageKeeperBot("Messages.db", "MessagesTable")

@bot.event
async def on_ready():
    print(f"Logged as XAV")


@bot.event
async def on_message(message):
    if message.author.bot or message.channel.type == discord.ChannelType.private:
        return
    
    # If the author is new, we register him
    if db.get_member(message.author.id) is None:
        register_member(message.author)
    
    # karma gestion
    if message.content.lower().split(" ")[0] in {"thx", "thanks", "ty"}:
        if message.mentions:
            done = []
            for member in message.mentions:
                if member.id in done:
                    continue

                if db.get_member(member.id) is None:
                    register_member(member)
                
                if member.id == message.author.id:
                    await message.channel.send("nerd")
                    return
                if member.bot:
                    await message.channel.send("bruh")
                    return
                
                db.update_member_karma(member.id, 1)
                done.append(member.id)

            await message.add_reaction("👍")

    await bot.process_commands(message)


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

async def money(ctx):
    await ctx.send(f"{guild.EMOJIS[858462619752857620]} https://www.youtube.com/watch?v=KigVdcSr8s4")


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

@bot.command()
async def s(contex):
    enemy = random.choice (["chihuahua", "border collie", "wolf"])
    father = random.choice (["John", "Mr.Pickles", "Hairyface", "Willy Wonka", "Steve", "Bob"])
    enemyadj = ["grimy", "muddy", "awful", "grotesque", "hideous", "adorable", "cute"]
    intro1 = "I was sitting on the edge of the rocky cliff beside my favourite tree."
    intro2 = "Alone in the searing desert, I was wondering why I was leaning against a cactus."
    intro3 = "Staring out my apartment window, I saw my reflection staring back at me."
    intro4 = "I was sitting in middle of aspire zone under a tree."
    char1 = "As I looked out into the distance, I thought about my past and all of the drama in it."
    char2 = "I wondered if this was my destiny- trying to find happiness."
    char3 = "I pulled out the photo of my long lost mother and where on earth she could be."
    prob1 = "Suddenly I was covered from head to toe with darkness. I couldn't breathe or see. Everything went black..."
    prob2 = "All of a sudden a psychopathic " + enemy + " grinned at me,showing all his razor sharp teeth. Suddenly it started"
    prob3 = "I suddenly felt a sharp needle sink into my flesh. It was a tranquilizer. But before I knew it I started feeling "
    sol1 = "I forced my drowsy eyes open my eyes to see a bright light."
    sol2 = "I forced my drowsy eyes open to find myself on the back of a massive dragon and a man in front of me."
    sol3 = "I forced my drowsy eyes open to the sounds of a " + random.choice(enemyadj) + " " +enemy + " licking my face."
    end1 = "A man came to my side with a knife. It was my friend!" + father + "!" "'Go to sleep young one...'"
    end2 = "It was difficult to keep my eyes open as I stuggled to breathe. "
    end3 = "A Man came and shoot a 3 bullets using a ak-47 . . ."

    intros = [intro1, intro2, intro3]
    characters = [char1, char2, char3]
    problems = [prob1, prob2, prob3]
    solutions = [sol1, sol2, sol3]
    endings = [end1, end2, end3]
    stor = (random.choice(intros) + random.choice(characters) + random.choice(problems) + random.choice(solutions) + random.choice(endings))
    print(random.choice(intros)),
    print(random.choice(characters)),
    print(random.choice(problems)),
    print(random.choice(solutions)),
    print(random.choice(endings))
    await contex.send(stor)
anime_list = ["Re:Zero − Starting Life in Another World.", "Death Note.", "Naruto.", "Ghost in the Shell.", "Steins;Gate.", "Fullmetal Alchemist.", "Samurai Champloo.", "Darker Than Black", "Magic kaito", "Konosuba", "Astolfo", "91 Days", "ACCA 13", "Aiura", "Ajin", "Akame ga Kill", "Amagi Brilliant Park", "Angel Beats", "Ano Natsu de Matteru", "Another", "B the Beginning", "Baka and Test", "Barakamon", "Ben-to", "Black Cat", "Black Lagoon", "Erased", "Bokura wa Minna Kawai-sou", "Bungou Stray Dogs", "Chuunibyo", "I don't understand What my Husband is Saying", "Daily Lives of Highschool Boys", "Darker than Black", "Death Note", "D-frag", "Fate stay night", "Millionaire Detective", "Full Metal Panic", "Fullmetal Alchemist", "Gakuen Babysitters", "Gate", "Gekkan Shoujo", "Ghost Hunt", "Gin no Saji", "Grisaia", "Hanasaku Iroha", "Demon Lord is a Part Timer", "Hellsing", "Hinamatsuri", "Hyouka", "Inou-battle", "Inu x Boku", "How not to Summon a Demon Lord", "One Week Friends", "Bofuri", "Kaguya Sama", "Maid Sama", "The World God Only Knows", "Kaze no Stigma", "Kekkai Sensen", "Kokoro Connect", "Konosuba", "Ghost in the Shell", "Beyond the Boundary", "Log Horizon", "Irregular at Magic High School", "Engaged to the Unidentified", "Minami-ke", "Problem Children", "Monster", "Musaigen no Phantom World", "Nanatsu no Taizai", "Nejimaki", "Net-juu", "No Game no Life", "Noragami", "Nurarihyon", "Wolf Children", "Overlord", "Papa no Iukoto wo Kikinasai", "Psycho-pass", "Re:Zero", "ReLife", "Rental Magica", "Rokka no Yuusha", "Rosario + Vampire", "Saenai Heroine (Saekano)", "School Days", "Seiken Tsukai mo World Break", "Your Lie in April", "Steins Gate", "Summer Wars", "SAO", "Tada Kun Never Falls in Love", "Tamako Market", "Slime Isekai", "The Pilot's Love Song", "The Princess and the Pilot", "To Aru Majutsu no Index", "To Aru Kagaku no Railgun", "To Aru Kagaku no Accelerator", "The Girl who leapt through time", "Tokyo Ravens", "Trigun", "Working", "Wotakoi", "Oregairu", "Tanya the Evil", "Toradora", "Arifureta", "Bottom tier character Tomozaki Kun", "The Day I Became a God", "Talentless Nana", "Tonari no Kaibutsu Kun", "Tokyo Ghoul", "Death Parade", "Parasyte the Maxim", "Hortensia Saga", "Isekai no Seikishi Monogatari"]
@bot.command(help="suggest an anime for You")
async def anime(message):
    await message.channel.send(random.choice(anime_list))
   
bot.run("")