from pyrogram import filters, Client

from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await client.join_chat("iwangid") 
        await client.join_chat("kazusupportgrp")
        await client.join_chat("kynansupport")
        await client.join_chat("amangsupportgrup")
        await client.join_chat("amwangs")
    except BaseException:
        pass
