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
        
            "`Communication is underway between the Joker and Mustafa...`",
            "`Call Connected.`",
            "`Joker: Hi Mustafa, how are you?`",
	    "`Mustafa: I'm good, and you?`",
	    "`Joker: I'm fine, I want to ask you about Ammar`",
	    "`Joker: Is it true that Ammar is a girl and not a man?`",
	    "`Mustafa: Yes it is🍑`",
	    "`Joker: خلاص ياعمي صدقت نفسك تتكلم الانجليزي`",
	    "`Mustafa: الي مايعرف انجليزي بهذا الوقت حمار`",
	    "`Joker: انت تعرف انجليزي ؟`",
	    "`Mustafa: انا حمار`",
            "`Joker: ونعم والله😂😂`",
	    "`Mustafa: الحين يجي الحرامي برلين ومعجون يسرقون كلامنا`",
            "`Joker: يرجال خلهم هذا قذرهم فقط السرقه`",
	    "`Joker: واذا استلمناهم واظهرنا الحقائق صارو يسبون الاهل والشرف 🤣🤣`",
	    "`Mustafa: تدري ليش يسبون الشرف ؟`",
            "`Joker: ليش ؟`",
	    "`Mustafa: لاان مايتكلم عن الشرف غير الي فاقده 😉`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
