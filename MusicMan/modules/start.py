# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Haii {message.from_user.first_name} My Name is jαyмυѕιcвoт ┏┛\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━
❃ Managed With ☕️ By : [ɢᴏᴊᴀʏ](https://t.me/ifcksht)
━━━━━━━━━━━━━━━
Ingin Menambahkan Saya ke Grup Anda? Tambahkan Saya Ke Group Anda!
</b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ 📜", url="https://t.me/jaymusichelp")
                  ],[
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ", url="https://t.me/enjoyinajasob"
                    ),
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url="https://t.me/ifcksht"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ 📜", url="https://t.me/jaymusichelp"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ", url="https://t.me/enjoyinajasob"
                    ),
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url="https://t.me/ifcksht"
                    )
                ]
            ]
        )
   )
