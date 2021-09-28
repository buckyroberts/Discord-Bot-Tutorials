import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='Welcome to the help section. Here are all the commands for this game!',
        color=discord.Colour.green()
    )
    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/8547538?s=259.1999931335449')
    embed.add_field(
        name='!help',
        value='List all of the commands',
        inline=False
    )
    embed.add_field(
        name='!punch',
        value='Punch another player',
        inline=False
    )
    embed.add_field(
        name='!roundhouse_kick',
        value='Roundhouse kick another player',
        inline=False
    )

    await ctx.send(embed=embed)


@bot.command()
async def punch(ctx, arg):
    """
    This command punches another player
    """

    await ctx.send(f'Punched {arg}')


@bot.command()
async def roundhouse_kick(ctx, *args):
    everyone = ', '.join(args)
    await ctx.send(f'Roundhouse kicked {everyone}')


bot.run('')
