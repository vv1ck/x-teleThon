#By STARKTM1
from telethon import events
import asyncio
import os
import sys
import time

@borg.on(events.NewMessage(pattern=r"\.plin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
        
        
    await event.edit("✈------------------")
    time.sleep(0.2)
    await event.edit("-✈-----------------")
    time.sleep(0.2)
    await event.edit("--✈----------------")
    time.sleep(0.2)
    await event.edit("---✈---------------")
    time.sleep(0.2)
    await event.edit("----✈--------------")
    time.sleep(0.2)
    await event.edit("-----✈-------------")
    time.sleep(0.2)
    await event.edit("------✈------------")
    time.sleep(0.2)
    await event.edit("-------✈-----------")
    time.sleep(0.2)
    await event.edit("--------✈----------") 
    time.sleep(0.2)
    await event.edit("---------✈---------")
    time.sleep(0.2)
    await event.edit("----------✈--------")
    time.sleep(0.2)
    await event.edit("-----------✈-------")
    time.sleep(0.2)
    await event.edit("------------✈------")
    time.sleep(0.2)
    await event.edit("-------------✈-----")
    time.sleep(0.2)
    await event.edit("--------------✈----")
    time.sleep(0.2)
    await event.edit("---------------✈---")
    time.sleep(0.2)
    await event.edit("----------------✈--")
    time.sleep(0.2)
    await event.edit("-----------------✈-")
    time.sleep(0.2)
    await event.edit("------------------✈@vv1ck")
    await asyncio.sleep(5)

