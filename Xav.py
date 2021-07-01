import discord
from discord.ext import commands
import random
import os

import db
from utils import Guild_utils


GUILD_ID = 700300301030391828
playing = False
wordlist = ['properly', 'identity', 'wood', 'tall', 'yellow', 'Marine', 'inner', 'wished', 'sounds', 'wagon', 'publication', 'Jews', 'rural', 'item', 'phone', 'attend', 'decisions', 'unable', 'faced', 'Republican', 'positions', 'huge', 'risk', 'supported', 'symbol', 'machines', 'description', 'seat', 'Smith', 'walking', 'Lake', 'trained', 'suggest', 'create', 'soil', 'interpretation', 'putting', 'forget', 'Dear', 'thoughts', 'preparation', 'Measurements', 'practices', 'experienced', 'Welfare', 'crowd', 'largest', 'Hudson', 'Massachusetts', 'Co', 'pushed', 'payment', 'handle', 'absence', 'prove', 'bitter', 'negative', 'vehicles', 'spend', 'January', 'remarks', 'assigned', 'Administrative', 'driving', 'grass', 'loose', 'wonderful', 'August', 'troops', 'band', 'chest', 'finding', 'slight', 'Japanese', 'windows', 'version', 'breakfast', 'What&#8217;s', 'sin', 'examples', 'experiences', 'depth', 'disease', 'wet', 'breath', 'Motors', 'practically', 'content', 'establishment', 'introduced', 'conflict', 'element', 'detailed', 'eventually', 'theater', 'correct', 'widely', 'hero', 'trust', 'raise', 'developing', 'Los', 'centers', 'Gold', 'dozen', 'telling', 'Alfred', 'bedroom', 'advanced', 'Detective', 'Indian', 'silence', 'contrary', 'characteristics', 'flesh', 'investigation', 'achieve', 'approval', 'estate', 'elections', 'Supreme', 'listen', 'conventional', 'gradually', 'David', 'views', 'foods', 'pull', 'October', 'Arthur', 'stream', 'Warren', 'advice', 'surprise', 'stages', 'player', 'guy', 'agree', 'uniform', 'abroad', 'devoted', 'papers', 'rear', 'cousin', 'situations', 'boats', 'ages', 'begun', 'colors', 'easier', 'shoulders', 'sick', 'nodded', 'opportunities', 'necessarily', 'angle', 'throat', 'waves', 'laughed', 'efficiency', 'automobile', 'mention', 'courts', 'issued', 'expense', 'extremely', 'fill', 'Institute', 'television', 'choose', 'Assembly', 'chain', 'Latin', 'Eisenhower', 'knowing', 'manufacturers', 'proud', 'wooden', 'worse', 'advertising', 'extra', 'Philadelphia', 'Angeles', 'pair', 'brilliant', 'conversation', 'taught', 'welcome', 'Hills', 'conviction', 'female', 'strike', 'burning', 'engine', 'Moments', 'Fundamental', 'tiny', 'desired', 'convinced', 'noticed', 'Till', 'towns', 'childhood', 'Protestant', 'employed', 'speaker', 'Constitution', 'passage', 'millions', 'Roberts', 'request', 'firmly', 'count', 'tendency', 'acceptance', 'driver', 'depends', 'ride', 'impressive', 'Sports', 'milk', 'Holy', 'tragedy', 'incident', 'operator', 'payments', 'creative', 'silent', 'measures', 'consideration', 'leaves', 'partly', 'Grand', 'suit', 'destroy', 'hoped', 'hopes', 'Royal', 'limit', 'operate', 'Twelve', 'Guard', 'integration', 'tired', 'screen', 'Mantle', 'Charlie', 'shooting', 'quietly', 'She&#8217;s', 'cry', 'via', 'pink', 'missile', 'functions', 'formal', 'occasionally', 'comparison', 'resistance', 'personality', 'concrete', 'precisely', 'plain', 'swung', 'sorry', 'maintained', 'drinking', 'intelligence', 'anger', 'poem', 'attitudes', 'liquid', 'Hearst', 'considering', 'bonds', 'denied', 'bills', 'employment', 'Cook', 'grant', 'fears', 'Cuba', 'sold', 'thousands', 'engaged', 'provision', 'purchase', 'safety', 'honest', 'representative', 'deny', 'Northern', 'Moscow', 'expenses', 'expansion', 'testimony', 'prior', 'blind', 'luck', 'lights', 'remarkable', 'surely', 'humor', 'Opera', 'Italian', 'singing', 'mail', 'Everywhere', 'vacation', 'Models', 'boards', 'supplies', 'stairs', 'ring', 'concentration', 'Congregation', 'rolled', 'unknown', 'movements', 'wearing', 'aspect', 'numerous', 'instrument', 'mere', 'essentially', 'soul', 'periods', 'patterns', 'odd', 'Lincoln', 'skin', 'Superior', 'relative', 'recommended', 'legislation', 'Georgia', 'bond', 'violence', 'insurance', 'opposition', 'creation', 'loan', 'dollar', 'difficulties', 'atomic', 'sheet', 'encourage', 'losses', 'trend', 'weakness', 'wave', 'identified', 'native', 'Avenue', 'decade', 'curious', 'anyway', 'engineering', 'pm', 'threw', 'flight', 'dangerous', 'award', 'ain&#8217;t', 'Wright', 'panels', 'seriously', 'liberty', 'shares', 'conscious', 'Salt', 'author', 'Chamber', 'centuries', 'equivalent', 'electrical', 'fought', 'pocket', 'fiction', 'doctrine', 'precision', 'artery', 'shut', 'offices', 'promised', 'promise', 'residential', 'adopted', 'taxes', 'load', 'depend', 'sum', 'Africa', 'impression', 'feels', 'referred', 'Edward', 'Calling', 'Pennsylvania', 'valuable', 'Alexander', 'Steel', 'charges', 'containing', 'target', 'includes', 'interference', 'TV', 'mounted', 'Cup', 'intended', 'Brain', 'qualities', 'offers', 'February', 'riding', 'Lucy', 'percentage', 'contain', 'Adams', 'expenditures', 'meat', 'Watson', 'elsewhere', 'prime', 'Ballet', 'cast', 'approached', 'angry', 'universal', 'terrible', 'medium', 'diameter', 'discovery', 'ice', 'curve', 'mold', 'burden', 'listed', 'warning', 'considerably', 'mostly', 'amounts', 'admitted', 'errors', 'wisdom', 'opinions', 'Asia', 'continuous', 'seeking', 'origin', 'Acres', 'changing', 'confusion', 'Orleans', 'hundreds', 'developments', 'enjoy', 'fired', 'younger', 'helping', 'pounds', 'nearby', 'accomplished', 'lies', 'suffering', 'em', 'lovely', 'snake', 'fun', 'sale', 'driven', 'spirits', 'ships', 'agent', 'collected', 'extensive', 'path', 'climbed', 'pilot', 'shoes', 'mobile', 'tables', 'expensive', 'Adam', 'arranged', 'volumes', 'answers', 'confused', 'contribute', 'Recognition', 'brush', 'Manchester', 'Hans', 'slaves', 'washing', 'oxygen', 'thickness', 'Mama', 'believes', 'mental', 'liquor', 'republic', 'lawyer', 'year&#8217;s', 'insisted', 'technology', 'bureau', 'route', 'explanation', 'dealing', 'rapid', 'salary', 'saved', 'transportation', 'reader', 'External', 'pace', 'recorded', 'iron', 'suffered', 'flying', 'dirt', 'year-old', 'yard', 'switch', 'concerns', 'separated', 'tour', 'dancing', 'comfort', 'Brothers', 'consists', 'warfare', 'investment', 'coat', 'raw', 'occur', 'reaching', 'grown', 'marketing', 'resulting', 'tend', 'drama', 'heads', 'identification', 'ie', 'lifted', 'catch', 'Mountains', 'recreation', 'heaven', 'readily', 'porch', 'cloth', 'darkness', 'Whenever', 'emotions', 'environment', 'appointed', 'prison', 'obtain', 'urban', 'smooth', 'holds', 'excess', 'waters', 'reply', 'unlike', 'reduction', 'comment', 'replaced', 'nineteenth', 'ease', 'throw', 'threat', 'demanded', 'lots', 'crossed', 'wire', 'muscle', 'o&#8217;clock', 'anybody', 'golden', 'Hardy', 'Anne', 'wages', 'hate', 'increasingly', 'bag', 'bound', 'express', 'regional', 'pride', 'engineer', 'sufficiently', 'distinguished', 'reflected', 'reactions', 'varying', 'varied', 'weapon', 'Journal', 'touched', 'guns', 'exists', 'editorial', 'seeds', 'possibilities', 'civilization', 'distinct', 'particles', 'Skill', 'fed', 'Rachel', 'anxiety', 'Linda', 'opposed', 'customers', 'proposal', 'storage', 'representatives', 'teach', 'societies', 'constantly', 'neighbors', 'removal', 'communities', 'vice', 'sell', 'Democrats', 'visited', 'writes', 'rough', 'steady', 'spending', 'Illinois', 'distinction', 'Francisco', 'Carl', 'arc', 'comparable', 'rare', 'continues', 'favorite', 'sake', 'display', 'Queen', 'downtown', 'restaurant', 'pleased', 'institution', 'assumption', 'seed', 'bread', 'match', 'musicians', 'remaining', 'Pike', 'shift', 'participation', 'virtually', 'stepped', 'limits', 'funny', 'smoke', 'involves', 'rarely', 'atoms', 'whereas', 'describe', 'cooling', 'tissue', 'Henrietta', 'Kate', 'combined', 'exception', 'Regarding', 'Highway', 'approved', 'personally', 'composed', 'senator', 'legislative', 'dependent', 'afford', 'Atlantic', 'Dean', 'happens', 'Walter', 'languages', 'goals', 'decide', 'notion', 'laboratory', 'proof', 'existed', 'Bob', 'Self', 'Grace', 'missed', 'prominent', 'code', 'thoroughly', 'shared', 'talent', 'studying', 'Handsome', 'automatic', 'burned', 'permanent', 'observations', 'drawing', 'Winston', 'desegregation', 'guidance', 'today&#8217;s', 'improvement', 'Treasury', 'presumably', 'bars', 'brings', 'Papa', 'indicates', 'discover', 'painted', 'intense', 'tool', 'necessity', 'eleven', 'shouted', 'focus', 'finger', 'conscience', 'criticism', 'psychological', 'thrown', 'glance', 'regions', 'stranger', 'joy', 'Pope', 'visual', 'parallel', 'shear', 'rode', 'Legislature', 'candidates', 'authorities', 'estimate', 'Lawrence', 'acts', 'improve', 'Ill', 'Rayburn', 'Cooperation', 'Communists', 'neutral', 'determination', 'deeply', 'assured', 'attractive', 'transfer', 'represents', 'newspapers', 'colleges', 'joint', 'Mississippi', 'severe', 'introduction', 'emergency', 'striking', 'trials', 'gained', 'contributed', 'mad', 'magazine', 'forever', 'mystery', 'selection', 'anywhere', 'furniture', 'agents', 'derived', 'revealed', 'provisions', 'guest', 'allotment', 'satisfactory', 'controlled', 'finish', 'maturity', 'concert', 'comedy', 'stick', 'Sleeping', 'listening', 'soldier', 'holes', 'Holmes', 'long-range', 'recall', 'mankind', 'destroyed', 'hydrogen', 'furthermore', 'objectives', 'defined', 'handling', 'Mayor', 'specifically', 'scheduled', 'accounts', 'districts', 'serving', 'leaned', 'experimental', 'tonight', 'track', 'Simultaneously', 'handed', 'copy', 'glad', 'Thompson', 'Paul', 'sharply', 'experts', 'reception', 'Temple', 'fifth', 'Robinson', 'Ohio', 'Cotton', 'attempts', 'sudden', 'bringing', 'sister', 'Foundation', 'ears', 'Japan', 'Palace', 'arrangements']
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
@bot.command()
async def hangman(ctx):
    global playing
    if playing == False:
        playing = True
        wrongcount = 6
        wrongletter = []
        word = (wordlist[random.randint(0, 848)])
        word = word.lower()
        length = len(word)
        letters = []
        letter = []
        for i in range(length):
            letters.append(word[i])
            letter.append("-")
        await ctx.send(str(length) + " letter word")
        await ctx.send(' '.join(letter))
        def checksender(msg):
            return msg.channel == ctx.channel and msg.author.name == ctx.message.author.name
        while playing:
            msg = await bot.wait_for('message', check=checksender)
            if (msg.content) == word:
                await ctx.send("correct! you won a big nothing congrats!!")
                playing = False
            elif len(msg.content) == 1:
                if (msg.content) in word:
                    for i in range(length):
                        if letters[i] == msg.content:
                            letter[i] = msg.content
                            await ctx.send(' '.join(letter))
                            if not "-" in letter:
                                await ctx.send("correct! you won a big nothing congrats!!")
                else:
                    if msg in wrongletter:
                        await ctx.send("you tried that before and it is wrong")
                    else:
                        wrongcount -= 1
                        wrongletter.append(msg)
                        await ctx.send("wrong you have " + str(wrongcount) + " tries left")
                        if wrongcount == 0:
                            await ctx.send("you lost ! the word was " + word)
                            playing = False
            elif msg.content == "hint":
                hint = False
                if wrongcount > 0:
                    while not hint:
                        randm = random.randint(0, length-1)
                        if letter[randm] == "-":
                            letter[randm] = word[randm]
                            wrongcount -= 1
                            await ctx.send(' '.join(letter) + " you have " + str(wrongcount) + " tries left")
                            hint = True
                else:
                    await ctx.send("sorry you only have 1 life left you have to guess")
            else:
                wrongcount -= 1
                await ctx.send("nope sowwy you have " + str(wrongcount) + " tries left :(")
                if wrongcount == 0:
                    await ctx.send("you lost ! the word was " + word)
                    playing = False 
bot.run(os.environ["TOKEN"])
