import discord
from discord.ext import commands

import db



class RoleReact(commands.Cog):
    def __init__(self, bot, guild):
        self.bot = bot
        self.guild = guild

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def rolereact(self, ctx, *msg):
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
            channel =  self.guild.guild.get_channel(channel_id)
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


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.bot.user.id:
            return

        msgid = payload.message_id
        info = db.get_rolereact_info(msgid)

        if info is None:
            return

        channel = self.guild.guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if str(payload.emoji) not in info['emojis']:
            if payload.emoji.name == "🗑️" and payload.user_id == info["creator"]:
                db.del_rolereact(msgid)
                for emoji in info['emojis']:
                    await message.remove_reaction(emoji, self.bot.user)
                
            await message.remove_reaction(payload.emoji, payload.member)
            return

        for emoji_name, role_id in zip(info['emojis'], info['roles']):
            if emoji_name == payload.emoji.name:
                break  # role_id will be kept in memory here
        
        # If the member already have the role we delete it, otherwise we add it.
        if role_id in list(map(lambda r: r.id, payload.member.roles)):
            await payload.member.remove_roles(self.guild.ROLES[role_id])
        else:
            await payload.member.add_roles(self.guild.ROLES[role_id])

        await message.remove_reaction(payload.emoji, payload.member)

