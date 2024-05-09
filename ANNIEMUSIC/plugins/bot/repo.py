from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

start_txt = """**
🫧 ωεℓ¢σмє ƒσя ɱσσɳ яєρσѕ 🫧

 ✰ ᴊɪᴛɴᴇ ʙʜɪ ɢᴄ ɴɪᴄᴄʜᴇ ᴅɪʏᴇ ʜᴀɪ ᴠᴏ sᴜʙ ᴊᴏɪɴ ᴋʀ ʟᴏ.....
 
 ✰ ᴀɢʀ ʀᴇᴘᴏ ᴄʜᴇɪʏᴇ ᴛᴏ ᴍᴏᴏɴ ᴋᴏ ᴅᴍ ᴋʀ ʟᴇ ᴠᴏ ᴅᴇ ᴅᴇɢᴀ ʀᴇᴘo...

 ✰ ʜᴇʀᴏᴋᴜᴇ ɪᴅ ᴄʜᴇɪʏᴇ ᴛᴏ ʙʜɪ ᴍᴏᴏɴ ᴋᴏ ᴅᴍ ᴋʀ ʟᴏ ᴍɪʟ ᴊᴀʏᴇɢɪ...
 
 ✰ ʏᴇ ʙᴏᴛ ᴀᴘɴᴇ ɢᴄ ᴍᴇ ᴀᴅᴅ ᴋʀ ʟᴇɴᴀ.....
 
 ✰ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss ᴏʀ ᴅᴍ...
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("🌊𝐓ᴀᴘ 𝐓o 𝐒ᴇᴇ 𝐓ʜᴇ 𝐌ᴀɢɪᴄ✨ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("💌 𝐇ᴇʟᴘ 💟", url="https://t.me/Grandxmasti"),
             InlineKeyboardButton("🕸 𝐃ᴇᴠᴇʟᴏᴘᴇʀ 🍃", url="https://t.me/Moonshining2"),
             ],
     
             [
             InlineKeyboardButton("💫 𝐌ᴏᴏɴ 𝐍ᴇᴛᴡᴏʀᴋ 🫧", url="https://t.me/Kittyxupdates"),
             ],
     
             [
             InlineKeyboardButton(" 𝐌ᴏᴏɴ🌙♡︎", url=f"https://t.me/Moonshining6"),            
             InlineKeyboardButton("︎🫧 𝐆ʀᴀɴᴅᴍᴀsᴛɪ 🫧", url=f"https://t.me/Grandxmasti"),
              ],
              
              [
              InclineKeyboardButton("𝐒ᴛᴜᴅʏ 𝐆ʀᴏᴜᴘ 𝟵𝐭𝐡,𝟭𝟬𝐭𝐡,𝟭𝟭𝐭𝐡",url=f"https://t.me/itz_PWM"),
              ]
       ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/58afe55fee5ae99d6901b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
