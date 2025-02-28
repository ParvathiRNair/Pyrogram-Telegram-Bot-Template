from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from Script import script
import asyncio
import sys
import os

START_TXT = script.START_TXT
HELP_TXT = script.HELP_TXT 
ABOUT_TXT = script.ABOUT_TXT

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
	await cmd.reply_text(
		START_TXT.format(cmd.from_user.first_name), 
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton("🔮Help", callback_data='help_cb'),
					InlineKeyboardButton("⚔About", callback_data='about_cb')
				],
				[
					InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/itzzzmeadarsh')
				]
			]
		)
	)
    
  
@Client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):	
	await cmd.reply_text(
		HELP_TXT, 
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton("⚔About", callback_data='about_cb'),
					InlineKeyboardButton("⚡Back", callback_data='start_cb')
				],
				[
					InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/itzzzmeadarsh')
				]
			]
		)
	)
