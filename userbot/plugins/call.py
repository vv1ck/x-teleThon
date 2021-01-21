"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`فلزا: هلا جوكر شخبارك ؟`",
            "`جوكر: والله تمام وانت ؟`",
            "`فلزا: تمام ، اسمع بقولك`",
            "`فلزا هذي قناتك ؟`  `@solo`",
            "`جوكر: لا ذا قروب المحنه بندول`",
            "`فلزا: اهااا عبالي قناتك`",    
            "`جوكر: لا انتبه واجد منتحلين`",
            "`فلزا: حاضر تاج راسي",
            "`فلزا: عندي مشكله ثانيه مب عارف اسوي بوت السبام`",
            "`جوكر: يافلزا يافلزا ازعجتني ترا`",
            "`فلزا ياخي شسوي ماعرفت ابيك تفهمني`",
            "`جوكر: حبيبي فلزا شرحت كيف الطريقة انا`",
            "`فلزا: وين شرحت ماشفت ؟؟`",
            "`جوكر: شرحتها بقناتي وين بعد`",
            "`فلزا: وشنو اسم قناتك طيببب؟؟؟`",
            "`جوكر: هذي قناتي انزل فيها الادوات واسوي شروحات @vv1ck`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
