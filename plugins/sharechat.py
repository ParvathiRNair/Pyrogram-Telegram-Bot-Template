from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from Script import script
import asyncio
import sys
import os
import requests
import re
@Client.on_message(filters.text)
async def share(bot, cmd):
	print(cmd)
	if "sharechat.com" in cmd.text:
		url = cmd.text
		rep = url.replace("post","video")
		response = requests.get(rep)
		video_url = re.search(r'property="og:video" content="(.*?)"', response.text).group(1)
		print(video_url);
		video_link = video_url
		await bot.send_video(chat_id=cmd.chat.id, video=video_url,caption="𝚃𝚑𝚊𝚗𝚔 𝚈𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙼𝚎🥰")
	elif "sharechat.com" not in cmd.text:
		await bot.send_message(chat_id=cmd.chat.id,text="What The Hell? Send ShareChat Video Link🚶❤️")
