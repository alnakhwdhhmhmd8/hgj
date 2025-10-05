import asyncio
import importlib
from pyrogram import idle
import config
from config import BANNED_USERS
from VeGaXMusic import HELPABLE, LOGGER, app, userbot
from VeGaXMusic.core.call import KIM
from VeGaXMusic.plugins import ALL_MODULES
from VeGaXMusic.utils.database import get_banned_users, get_gbanned

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VeGaXMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("VeGaXMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("VeGaXMusic.plugins").info("Successfully Imported All Modules ")
    await userbot.start()
    await KIM.start()
    await KIM.decorators()
    LOGGER("VeGaXMusic").info("VeGaXMusic By: [ @wwvvwt ]")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("VeGaXMusic").info("Stopping VeGaXMusic! GoodBye")

print("""

───▟████▙──────────▟██▙─────▟████▙───━▟████▙──────────────▟████▙───
───██──██──────────█▛▜█─────█▛▀▀▜█────██──██──────────────█▉──██────
───██──██─────────██─▟█─────█▙▄▄▟█────█▉───██────────────██───█▉────
───██──██────────██──▟█─────▜████▛────██────██──────────██────██────
───██──██───────██──██────────────────██─────██────────██─────█▉────
───██──██──────██──██───────▟████▙────██──────██──────██──────█▉────
───██──██─────██──██────────██──██────██───────██────█▉───────██────
───██──██────██──██─────────██──██────██────────██──██────────██────
───██──██───██──██──────────██──██────██──▟█▙────█▙▟▉────▟█▙──██────
───██──██──██──██───────────██──██────██──▜█▛─────▜▛─────▜█▛──█▉────
───██──▟█▙█▛──██────────────██──██────██──▟▉█▙──────────▟▉█▙──██────
───██──▜█▛──▟█▛─────────────██──██────██──██─██────────██─██──██────
───██───────▜█──────────────██──██────██──██──██──────██──██──██────
───██──▟█▙──▟█──────────────██──██────██──██───██────██───█▉──█▉────
───██──▜█▛█▙▜█▙─────────────██──██────██──█▉────█▙──▟█────██──██────
───██──██─██──██────────────██──██────██──██─────▜▙▟▛─────█▉──██────
───██──██──██──██───────────██──██────██──██──────▜▛──────█▉──██────
───██──██───██──██──────────██──██────██──██──────────────██──█▉────
───██──██────██──██─────────██──██────██──██──────────────██──██────
───██──██─────██──██────────██──██────██──██───[ @wwvvwt ]──██──██────
───██──██──────██──██───────██──█▉────██──█▉──────────────██──██────
───██──██───────██─██───────██──██────██──█▉──────────────██──██────
───██──██───────▜▙─▟▛───────██──█▉────██──██──────────────██──██────
───▜████▛────────▜█▛───██───▜████▛────▜████▛──────────────▜████▛──[ By
 
(2024-2025) 𝙗𝙮: @wwvvwt
𝙂𝙧𝙚𝙚𝙩𝙞𝙣𝙜𝙨 𝙛𝙧𝙤𝙢 : 𝐉𝐀𝐊
  """)