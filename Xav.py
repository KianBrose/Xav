import discord
from discord.ext import commands
import random
import os

import db
from utils import Guild_utils


GUILD_ID = 700300301030391828

bot = commands.Bot(command_prefix='€')
guild = Guild_utils(bot, GUILD_ID)
db.init()

def register_member(member):
    id = member.id
    name = member.name
    roles = list(map(lambda r: r.id, member.roles))
    db.add_member(id, name, roles)


@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")


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
    await ctx.send(random.choices(['Welcome', 'Welcum'], [0.99, 0.01])[0])  # 1% chance of saying "Welcum"


@bot.command()
async def money(ctx):
    await ctx.send(" <:pepeEvil:859652252040691712> https://www.youtube.com/watch?v=KigVdcSr8s4")

@bot.command()
async def karma(ctx):
    await ctx.send(f"You have : {db.get_member(ctx.author.id)['karma']} karmas")

@bot.command()
async def h(ctx):
    await ctx.send(random.choices(['hello', 'hello world'], [0.60, 0.40]))
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
   
bot.run(os.environ["TOKEN"])
