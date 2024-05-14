import random
from pyrogram import filters
from ANNIEMUSIC import app
from ANNIEMUSIC import *
from ... import *
import config

from ...logging import LOGGER

from ANNIEMUSIC import app, userbot
from ANNIEMUSIC.core.userbot import *

import asyncio

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
from ANNIEMUSIC.core.userbot import Userbot
from datetime import datetime

# Assuming Userbot is defined elsewhere
userbot = Userbot()


BOT_LIST = ["[🇲σ᭡፝֟ɳ🌙](https://t.me/Moonshining2)", "[˹𝐊íԵԵყ ✘ 𝙼ᴜsɪᴄ˼](https://t.me/kittyxmusic_bot)", "[˹ 𝐊íԵԵყ ✘ Chat ˼](https://t.me/kittyxchat_bot", "[˹sᴛꝛɪɴɢ ғᴧᴛʜᴇꝛ ʙᴏᴛ˼](https://t.me/StringxFatherBot)", "[ᴋɪᴛᴛʏ ᴜᴘᴅᴀᴛᴇs](https://t.me/kittyxupdates)"]

@app.on_message(filters.command("botschk") & filters.user(OWNER_ID))
async def bots_chk(_, message):
    msg = await message.reply_photo(photo="https://telegra.ph/file/4d303296e4fac9a40ea07.jpg", caption="**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ...**")
    response = "**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ @Kittyxupdates**\n\n"
    for bot_username in BOT_LIST:
        try:
            bot = await app.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await app.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            async for bot_message in app.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ❌**\n"
    
    await msg.edit_text(response)
                
