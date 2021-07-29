import discord
from discord.ext import commands
import random
import os

import db
from utils import Guild_utils


GUILD_ID = 711325947269349448
PREFIX = '€'
intents = discord.Intents(messages=True, guilds=True, reactions=True)

bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command('help')

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


@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return

    msgid = payload.message_id
    info = db.get_rolereact_info(msgid)

    if info is None:
        return

    channel = guild.guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if str(payload.emoji) not in info['emojis']:
        if payload.emoji.name == "🗑️" and payload.user_id == info["creator"]:
            db.del_rolereact(msgid)
            for emoji in info['emojis']:
                await message.remove_reaction(emoji, bot.user)
            
        await message.remove_reaction(payload.emoji, payload.member)
        return

    for emoji_name, role_id in zip(info['emojis'], info['roles']):
        if emoji_name == payload.emoji.name:
            break  # role_id will be kept in memory here
    
    # If the member already have the role we delete it, otherwise we add it.
    if role_id in list(map(lambda r: r.id, payload.member.roles)):
        await payload.member.remove_roles(guild.ROLES[role_id])
    else:
        await payload.member.add_roles(guild.ROLES[role_id])

    await message.remove_reaction(payload.emoji, payload.member)



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
    await ctx.send(f"{guild.EMOJIS['pepeEvil']} https://www.youtube.com/watch?v=KigVdcSr8s4")


@bot.command()
async def karma(ctx):
    await ctx.send(f"You have : {db.get_member(ctx.author.id)['karma']} karmas")


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def rolereact(ctx, *msg):
    if not (3 <= len(msg) <= 4):
        await ctx.send("Error in the command.\nUsage: ``€rolereact message_link emoji1-emoji2 @role1-@role2``")
        return 

    try:
        link = msg[0].split('/')
        msgid = int(link[-1])
        channel_id = int(link[-2])
    except ValueError:
        await ctx.send("Error in the link, nerd")
        return 
    
    if db.get_rolereact_info(msgid) is not None:
        await ctx.send("This message has already an event binded.")
        return
    
    emojis = msg[1].split("-")
    creator_id = ctx.author.id

    if "🗑️" in emojis:
        await ctx.send("You can't use this emoji !")
        return

    try:
        channel =  guild.guild.get_channel(channel_id)
        for emoji in emojis:
            message = await channel.fetch_message(msgid)
            await message.add_reaction(emoji)
    except discord.errors.HTTPException:
        await ctx.send("Please use correct emojis !")
        return

    roles = ctx.message.raw_role_mentions
    if len(roles) != len(emojis):
        await ctx.send("You need to have as many roles as emojis")
        return
    
    db.add_rolereact(msgid, emojis, roles, creator_id)

    await ctx.channel.send("Done ! React to the message with 🗑️ to delete the role react event")


@bot.command()
async def pool(ctx, *question):
    await ctx.message.delete()

    embed = discord.Embed(title=f"suggestion from {ctx.author.name}", desc="suggestion", color=0x34a1eb)
    embed.add_field(name=f"{' '.join(question)}\u200b\u200b", value="Answer with the reactions below.")

    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await message.add_reaction("❌")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commands available", color=0x34a1eb)

    embed.add_field(name=f"{PREFIX}info", value="display the info message")
    embed.add_field(name=f"{PREFIX}tos", value="display the tos message")
    embed.add_field(name=f"{PREFIX}w", value="display the welc~~um~~ome message")
    embed.add_field(name=f"{PREFIX}money", value="CAPITALISM")
    embed.add_field(name=f"{PREFIX}karma", value="check your current karma")
    embed.add_field(name=f"{PREFIX}pool <question>", value="create a pool")
    embed.add_field(name=f"{PREFIX}rolereact <message link> <emojis> <roles>", value="create a role react event (admin only)")

    await ctx.send(embed=embed)


bot.run(os.environ["TOKEN"])
