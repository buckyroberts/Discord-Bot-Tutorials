import discord

"""
client = discord.Client()

@client.event
async def on_ready():
    print('Ready')

client.run('')
"""


# https://discordpy.readthedocs.io/en/latest/intents.html
# https://discord.com/developers/docs/topics/gateway#gateway-intents
# https://discord.com/developers/docs/topics/gateway#list-of-intents


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 891404574114594836

    async def on_ready(self):
        print('Ready')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Potato person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Chocolate lover')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='Funky monkey')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Potato person')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Chocolate lover')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='Funky monkey')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('')
