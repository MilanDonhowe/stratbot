#****************************************************************
# Filename: Bot.py
# Author: Milan Donhowe
# Date: 6/12/2020
# Description: discord bot interface driver using discord.py's
#              commands extension
#****************************************************************

import discord
from discord.ext import commands
from stratRouletteBot.bot.strategies.Strategies import Strategies

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Stratbot logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Game(name="hunt the wumpus |!help"))

# add strategies command
bot.add_cog(Strategies(bot))


@bot.event
async def on_command_error(ctx, err):
    if (isinstance(err, commands.CommandNotFound)):
        return
    if (isinstance(err, commands.MissingRequiredArgument)):
        return
    if (isinstance(err, commands.BadArgument)):
        return
    raise err




