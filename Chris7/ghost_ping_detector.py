from discord import TextChannel, Embed
from discord.ext import commands


class GhostPingDetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        if message.mentions or message.role_mentions:
            if message.mentions and all(mention.id == message.author.id or mention.bot for mention in message.mentions):
                return

            replied_to_message = None
            replied_to_user = None

            if message.reference and message.reference.message_id and message.reference.guild_id == message.guild.id:
                replied_to_channel = message.guild.get_channel(message.reference.channel_id)
                if isinstance(replied_to_channel, TextChannel):
                    replied_to_message = await replied_to_channel.fetch_message(message.reference.message_id)
                    replied_to_user = replied_to_message.author

            if replied_to_user and replied_to_user.bot:
                return

            embed = Embed(colour=0x35BC31, title='Ghost Ping Detected!')

            if replied_to_user:
                embed.add_field(name='Author', value=message.author)
                embed.add_field(name='Reply to', value=replied_to_user)
            else:
                embed.add_field(name="Author", value=message.author, inline=False)

            embed.add_field(name='Message', value=message.content, inline=False)

            if replied_to_message:
                embed.add_field(name='Message replied to',
                                value=f'https://discord.com/channels/{replied_to_message.guild.id}/{replied_to_message.channel.id}/{replied_to_message.id}')

            embed.set_footer(text=f'Message sent at {message.created_at}')

            await message.channel.send(embed=embed)
