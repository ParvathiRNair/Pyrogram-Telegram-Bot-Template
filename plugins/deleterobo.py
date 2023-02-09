import pyrogram
import time
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from Script import script
import asyncio
import sys
import os
import requests
import re
# Connect to MongoDB
client = MongoClient("mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")
db = client["mydatabase"]
collection = db["group_timers"]

@Client.on_message(filters.group)
def delete_after_time(client, message):
    group_id = message.chat.id
    
    # Check if there's a timer set for this group
    timer = collection.find_one({"group_id": group_id})
    
    if timer:
        # Calculate the time difference
        now = time.time()
        time_difference = now - message.date
        
        # If the time difference is greater than the timer, delete the message
        if time_difference > timer["time"]:
            client.delete_messages(chat_id=group_id, message_ids=message.message_id)
@Client.on_message(filters.command("set_timer"))
def set_timer(client, message):
    # Check if the user is an administrator
    if message.chat.type == "group" and message.from_user.status in ["administrator", "creator"]:
        # Extract the timer value from the message
        timer = int(message.text.split(" ", 1)[1])
        
        # Update or insert the timer in the database
        collection.update_one({"group_id": message.chat.id}, {"$set": {"group_id": message.chat.id, "time": timer}}, upsert=True)
        
        # Confirm the timer has been set
        client.send_message(chat_id=message.chat.id, text="Timer set successfully!")

app.run()
