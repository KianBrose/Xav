import discord
from discord.ext import commands
import asyncio
import random


def convert(time_str):
	converted = -1
	time_symbols = {'d': 3600*24,
					'h': 3600,
					'm': 60,
					's': 1}

	for symbol in time_symbols.keys():
		data = time_str.split(symbol)

		if len(data) > 2:
			return -1

		if len(data) == 2:
			time_str = data[1]

		if len(data) == 1:
			continue

		try:
			converted += int(data[0]) * time_symbols[symbol]
		except ValueError:
			return -1

	return converted


class Giveway(commands.Cog):
    def __init__(self, bot, guild):
        self.bot = bot
        self.guild = guild

    @commands.command()
    async def giveway(self, ctx, time_left, prize, *text):
        await ctx.message.delete()

        converted_time = convert(time_left)
        if converted_time == -1:
            await ctx.author.send("Please provide a correct time when starting a giveway.")
            return

        embed = discord.Embed(title=f"New Giveway ! 🎉", description=f"{' '.join(text)}\n" if text else None, color=0x34a1eb)

        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        embed.add_field(name=f"PRIZE : **{prize}**", value="Participate with the reaction below.", inline=False)
        embed.set_footer(text=f"Ends in : {time_left}")

        message = await ctx.send(embed=embed)
        await message.add_reaction("🐸")


        await asyncio.sleep(converted_time)

        msg = await ctx.channel.fetch_message(message.id)
        reactions = await msg.reactions[0].users().flatten()
        reactions.pop(0)

        if not reactions:
            await ctx.channel.send("No on won. :(")
            return

        chosen_one = random.choice(reactions)

        await ctx.channel.send(f"Poggers to {chosen_one.mention} for winning the giveway ! Feel free to DM {ctx.author.mention} to claim your prize 🎉")


    @commands.command()
    async def reroll(self, ctx, msg_link):
        try:
            link = msg_link.split('/')
            msgid = int(link[-1])
            channel_id = int(link[-2])
        except ValueError:
            await ctx.author.send("Error in the link, nerd")
            await ctx.message.delete()
            return 

        channel = self.guild.guild.get_channel(channel_id)
        message = await channel.fetch_message(msgid)

        reactions = await message.reactions[0].users().flatten()
        reactions.pop(0)

        if not reactions:
            await ctx.channel.send("No on won. :(")
            return

        chosen_one = random.choice(reactions)

        await ctx.channel.send(f"After a reroll, now it's {chosen_one.mention} turn to win ! Congrats to him and don't forget to DM {ctx.author.mention} to claim the prize")


        
