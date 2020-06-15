#****************************************************************
# Filename: __main__.py
# Author: Milan Donhowe
# Date: 6/12/2020
# Description: Entry point for discord bot
#****************************************************************
from stratRouletteBot.bot.bot import bot
from os import environ

if __name__ == "__main__":
    print("Running strat bot")
    # Client Token is loaded as a environmental variable DISCORD_BOT_TOKEN
    bot.run(environ["DISCORD_BOT_TOKEN"])