import discord
from discord.ext import commands


class Pool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pool(self, ctx, *question):
        await ctx.message.delete()

        embed = discord.Embed(title=f"suggestion from {ctx.author.name}", desc="suggestion", color=0x34a1eb)
        embed.add_field(name=f"{' '.join(question)}\u200b\u200b", value="Answer with the reactions below.")

        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")
