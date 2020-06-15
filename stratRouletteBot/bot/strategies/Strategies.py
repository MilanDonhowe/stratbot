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
from stratRouletteBot.util.cache import Cache



class Strategies(commands.Cog):
    """Commands to get unique strategies for particular CSGO maps."""
    def __init__(self, bot):
        self.bot = bot
        # strat_cache to prevent multiple strats being chosen
        self.strat_cache = Cache(5)

    
    async def pick_strategy(self, strategies):
        """Randomly selects a strategy not present in the cache"""
        index = randint(0, len(strategies)-1)
        og_index = index
        while (strategies[index] in self.strat_cache):
            index += 1
            if (index >= len(strategies)):
                index = 0
            if (index == og_index):
                break
        return strategies[index]




    @commands.command(
        brief = "--> sends DM to user containing a random strategy.",
        help = "Sends DM to user containing a random strategy.  For example, the command: \"!strat t de_dust2\" "\
        "will result in the bot sending you a personal message with a random strategy for terrorists on dust 2"
    )
    async def strat(self, ctx, side, map="general", pistols_only=False):
        strategies = await query_strats(map, side, pistols_only)

        if (len(strategies) == 0):
            await ctx.send("Sorry, no strategies could be found for that map/side.")
        else:         
            random_strat = await self.pick_strategy(strategies)
            self.strat_cache.add(random_strat)
            await ctx.author.send(f"**{random_strat[0]}**: {random_strat[1]}")

    @commands.command()
    async def strats(self, ctx, side, map="general", pistols_only=False):
        await self.strat(ctx, side, map, pistols_only)

    @strat.error
    @strats.error
    async def strat_error(self, ctx, err):
        if (isinstance(err, commands.BadArgument)):
            await ctx.send("Sorry I couldn't find any " + str(err))
        elif (isinstance(err, commands.MissingRequiredArgument)):
            await ctx.send("Error: not enough arguments given.")
