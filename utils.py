class Guild_utils(object):
    """
    Just because it's only pain to access roles or channels through id's
    this is a quick fix to make life easier.
    usage:
    >>> guild = Guild_utils(bot, guild_id)
    >>> guild.ROLES["ACTIVE"]  # get the active role object
    >>> guild.CHANNELS["suggestions"]  # get the suggestion channel (don't have to type the emoji)
    >>> guild.guild  # the actual guild object, you can access all methods of discord.Guild through here
    """
    def __init__(self, bot, guild_id):
        self.bot = bot
        self.guild_id = guild_id
    
    @property
    def guild(self):
        return self.bot.get_guild(self.guild_id)

    @property
    def ROLES(self):
        roles = {}

        for role_name, role in list(map(lambda r: (r.name, r), self.guild.roles)):
            roles[role_name] = role
        
        return roles

    @property
    def CHANNELS(self):
        channels = {}

        for channel_name, channel in list(map(lambda c: (c.name, c), self.guild.channels)):
            # We don't have to type the emojis to get role, only the regular
            # name like "gaming-chat" or "main-chat"
            quick_name = "┇".join(channel_name.split("┇")[1:])  # joining ┇ in case there 
                                                                # is actually a ┇ char in the name but yeah
            channels[quick_name] = channel

        return channels
