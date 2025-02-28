# Add bot's callbacks command here

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters
from Script import script
import asyncio
import sys
import ast
import os
import re

START_TXT = script.START_TXT
HELP_TXT = script.HELP_TXT 
ABOUT_TXT = script.ABOUT_TXT

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "help_cb":
        buttons = [
          [
            InlineKeyboardButton("⚔About", callback_data='about_cb'),
            InlineKeyboardButton("⚡Back", callback_data='start_cb')
          ],
          [
            InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/itzzzmeadarsh')
          ],
          [
            InlineKeyboardButton("🧿Close", callback_data='close')
          ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=HELP_TXT,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    
    elif query.data == "about_cb":
        buttons = [
          [
            InlineKeyboardButton("🔮Help", callback_data='help_cb'),
            InlineKeyboardButton("⚡Back", callback_data='start_cb')
          ],
          [
            InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/itzzzmeadarsh')
          ],
          [
            InlineKeyboardButton("🧿Close", callback_data='close')
          ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=ABOUT_TXT,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    
    elif query.data == "start_cb":
        buttons = [
          [
            InlineKeyboardButton("🔮Help", callback_data='help_cb'),
            InlineKeyboardButton("⚔About", callback_data='about_cb')
          ],
          [
            InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/itzzzmeadarsh')
          ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="𝙸'𝚊𝚖 𝙰 𝚂𝚞𝚙𝚎𝚛𝚏𝚊𝚜𝚝 𝚂𝚑𝚊𝚛𝚎𝙲𝚑𝚊𝚝 𝚅𝚒𝚍𝚎𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚛 𝚆𝚒𝚝𝚑𝚘𝚞𝚝 𝚆𝚊𝚝𝚎𝚛𝚖𝚊𝚛𝚔.",
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        
    elif query.data == "close":
        await query.message.delete()
