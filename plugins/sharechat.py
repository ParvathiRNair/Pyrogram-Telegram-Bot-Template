from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from Script import script
import asyncio
import sys
import os

@Client.on_message(filters.text)
async def share(bot, cmd):
	print(cmd)
