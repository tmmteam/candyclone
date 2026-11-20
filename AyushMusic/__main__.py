
import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AyushMusic import LOGGER, app, userbot
from AyushMusic.core.call import Aayu
from AyushMusic.misc import sudo
from AyushMusic.plugins import ALL_MODULES
from AyushMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from AyushMusic.plugins.tools.clone import restart_bots


async def init():
    if not config.STRING1:
        LOGGER(__name__).error("String Session not filled, please Provide a valid session.")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AyushMusic.plugins" + all_module)
    LOGGER("AyushMusic.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await Aayu.start()
    try:
        await Aayu.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AyushMusic").warning(
            "⚠️ Log group voice chat is not active! Please start voice chat in your logger group to enable streaming."
        )
    except Exception as e:
        LOGGER("AyushMusic").warning(f"⚠️ Initial stream call warning: {e}")
    await Aayu.decorators()
    await restart_bots()
    LOGGER("AyushMusic").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 AYUSH☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AyushMusic").info("𝗦𝗧𝗢𝗣 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
