#****************************************************************
# Filename: Strategies.py
# Author: Milan Donhowe
# Date: 6/13/2020
# Description:  Cog class to encapsulate strategy bot commands
#               
#****************************************************************

from discord.ext import commands
from random import randint
from stratRouletteBot.db.stratsAPI import query_strats


class Strategies(commands.Cog):
    """Commands to get unique strategies for particular CSGO maps."""
    def __init__(self, bot):
        self.bot = bot
        # strat_cache to prevent multiple strats being chosen
        self.strat_cache = set()

    @commands.command(
        brief = "--> sends DM to user containing a random strategy.",
        help = "Sends DM to user containing a random strategy.  For example, the command: \"!strat de_dust2 T\" "\
        "will result in the bot sending you a personal message with a random strategy for terrorists on dust 2"
    )
    async def strat(self, ctx, map, side, pistols_only=False):
        strategies = await query_strats(map, side, pistols_only)

        if (len(strategies) == 0):
            await ctx.send("Sorry, no strategies could be found for that map/side.")
        else:
            strat_index = randint(0, len(strategies)-1)
            strat_name = strategies[strat_index][0]
            strat_desc = strategies[strat_index][1]
            await ctx.author.send(f"**{strat_name}**: {strat_desc}")


    @strat.error
    async def strat_error(self, ctx, err):
        if (isinstance(err, commands.BadArgument)):
            await ctx.send("Sorry I couldn't find any " + str(err))
