import os 
from pyrogram import Client
from pyrogram import idle
from pyromod import listen
from Maker import *
from pyromod import listen
from pyrogram.errors import PeerIdInvalid, ChatWriteForbidden
from Maker import *
from asBASE import asJSON
from asyncio import sleep

db = asJSON("as.json")

TOKEN = "8469110218:AAFWdVLT_4iidXFmuS1UaPEr0ItuZivSjCs"

SUDORS = [7623838169, 8122544723, 8176410693]
DEVS = ["wwvvwt","wwvvwt","wwvvwt"]

bot = Client(
    "VeGa",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token=TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: ✨ STARTING BOT [ VEGA ]")
    await bot.start()
    for dev_id in DEVS:
        try:
            msg = await bot.send_message(dev_id, "⚡️")
            await sleep(5)
            await msg.delete()
            await bot.send_message(dev_id, "<blockquote>ꜱᴇʀᴠᴇʀ ᴄᴏɴᴛᴀᴄᴛᴇᴅ⟲</blockquote>")
            print(f"[INFO]: Successfully notified developer @{dev_id}")
        except PeerIdInvalid:
            print(f"[ERROR]: Invalid developer ID: @{dev_id}")
        except ChatWriteForbidden:
            print(f"[ERROR]: Cannot write to chat with developer: @{dev_id}")
        except Exception as e:
            print(f"[ERROR]: Error while handling developer @{dev_id}: {e}")

    await idle()

bot_id = TOKEN.split(":")[0]


