#****************************************************************
# Filename: __main__.py
# Author: Milan Donhowe
# Date: 6/12/2020
# Description: Entry point for discord bot
#****************************************************************
from stratRouletteBot.bot.bot import bot

if __name__ == "__main__":
    print("Running strat bot")
    bot.run("YOUR-CLIENT-TOKEN-HERE")