from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command()
async def punch(ctx, arg):
    """
    !punch Justin
    """

    await ctx.send(f'Punched {arg}')


@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch Justin Hussu
    """

    await ctx.send(f'Double punched {arg1} and {arg2}')


@bot.command()
async def roundhouse_kick(ctx, *args):
    """
    !roundhouse_kick Justin Hussu Magnetic Kristy
    """

    everyone = ', '.join(args)
    await ctx.send(f'Roundhouse kicked {everyone}')


@bot.command()
async def info(ctx):
    """
    ctx - context (information about how the command was executed)

    !info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


bot.run('')
