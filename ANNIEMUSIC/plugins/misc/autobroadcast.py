import asyncio
import datetime
from ANNIEMUSIC import app
from pyrogram import Client
from config import START_IMG_URL
from ANNIEMUSIC.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""**MESSAGE = f"""**╭───────────────────⦿\n├───────────────────⦿\n│☄️ ▸ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs\n│✨ ▸ ᴀʟʟ-ɪɴ-ᴏɴᴇ ʙᴏᴛ\n├───────────────────⦿\n│🌴 ▸ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs\n│💫 ▸ ᴄʜᴀᴛ-ʙᴏᴛ + ᴍᴜsɪᴄ-ʙᴏᴛ\n│💤 ▸ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ\n│🍁 ▸ ɢᴇɴᴇʀᴀᴛᴏʀ ɪᴍᴀɢᴇs + ᴛᴀɢ ᴀʟʟ\n│🌠 ▸ ᴡᴇʟᴄᴏᴍᴇ + ʟᴇғᴛ ɴᴏᴛɪᴄᴇ\n│🕳️ ▸ 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ\n├───────────────────⦿\n│🍷 ᴛᴀᴘ ᴛᴏ ᴄᴏᴍᴍᴀɴᴅs ᴍʏ ᴅᴇᴀʀ\n│🍹 ᴍᴀᴅᴇ ʙʏ🪽 ➪ [🇲σ᭡፝֟ɳ🌙♡︎](https://t.me/Moonshining2)\n╰───────────────────⦿

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("˹🕸️ ᴛᴧᴘ тᴏ sᴇᴇ ᴍᴧɢɪᴄ 🕸️˼", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 1 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats
async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(180000)  # Sleep (180000 seconds) between next broadcast

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())
