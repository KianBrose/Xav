import discord
from discord.ext import commands

import db


def register_member(member):
    id = member.id
    name = member.name
    roles = list(map(lambda r: r.id, member.roles))
    db.add_member(id, name, roles)


class Karma(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
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

        # await self.bot.process_commands(message)

    @commands.command()
    async def karma(self, ctx):
        member = db.get_member(ctx.author.id)

        if member is None:
            register_member(ctx.message.author)
            member = db.get_member(ctx.author.id)

        await ctx.send(f"You have : {member['karma']} karmas")
