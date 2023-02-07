from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from Script import script
import asyncio
import sys
import os

@Client.on_message(filters.text)
async def share(bot, cmd):
	print(cmd)
	if "sharechat.com" in cmd.text:
	    url = cmd.text;
	    rep = url.replace("post","video")
	    response = requests.get(rep)
	    video_url = re.search(r'property="og:video" content="(.*?)"', response.text).group(1)
	    print(video_url);
	    video_link = video_url
	    bot.send_video(chat_id=message.chat.id, video=video_url,caption="Thank You For Using Me :)")
