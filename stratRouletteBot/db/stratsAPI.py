#****************************************************************
# Filename: stratsAPI.py
# Author: Milan Donhowe
# Date: 6/11/2020
# Description:  functions for managing interactions with strategy database
#               and validating valid queries
#****************************************************************

import asyncio
import aiosqlite
from discord.ext.commands import BadArgument

# if either valid functions find an error they should raise an exception

async def valid_map(map):
    """determines if a given map string is valid and returns associated map key"""

    map_key = {
        "dust":"de_dust2",
        "inferno":"de_inferno",
        "overpass":"de_overpass",
        "mirage":"de_mirage",
        "cache" : "de_cache",
        "nuke": "de_nuke",
        "office": "de_office",
        "anubis": "de_anubis"
    }

    for k in map_key.keys():
        if k in map:
            return map_key[k]

    raise BadArgument(message=f'map named {map}')


async def valid_side(side):
    """determines if a given team is valid and returns associated team key"""
    
    side = side.strip().upper()
    if (side in ("T", "CT")):
        return side
    
    raise BadArgument(message='team side named {side} (Acceptable team sides are "T" or "CT")')



async def query_db(v_map, v_side, pistol_flag):
    """connects to strats.db and returns obtained strategies"""
 
    conn = await aiosqlite.connect("strats.db")
    curs = await conn.cursor()
    
    if (pistol_flag == False):
        await curs.execute(f'SELECT STRAT_NAME, STRAT FROM strats WHERE ((MAP == "gen") OR (MAP == "{v_map}")) AND SIDE == "{v_side}"')
    else:
        await curs.execute(f'SELECT STRAT_NAME, STRAT FROM strats WHERE ((MAP == "gen") OR (MAP == "{v_map}")) AND SIDE == "{v_side}" AND PISTOLS==1')

    results = await curs.fetchall()
    await curs.close()
    await conn.close()
    
    return results


async def query_strats(map, side, pistols_flag):
    """retrieves list of strategies based on map & side"""
    db_map = await valid_map(map)
    db_team = await valid_side(side)
    return await query_db(db_map, db_team, pistols_flag)
