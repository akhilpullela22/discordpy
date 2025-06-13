import discord
import random
import datetime
import os
import asyncio
#from bs4 import BeautifulSoup
#from googletrans import Translator
import requests
from discord.ext import commands

with open("C:\\Users\\akhil\\Documents\\Bot_keys\\bot_token.txt", "r") as file:
    Token = file.read()
with open("C:\\Users\\akhil\\Documents\\Bot_keys\\tba_auth.txt", "r") as file:
    auth_key = file.read()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if '!team' in message.content:
            parts = message.content.split(" ", 1)  # Split at the first space
            if len(parts) > 1:
                number = parts[1]
            try:
                int(number)
                response = requests.get(f"https://www.thebluealliance.com/api/v3/team/frc{number}",
                headers={
                "X-TBA-Auth-Key": auth_key}
                )
                json_parsed = response.json()
                embed = discord.Embed(title = 'Team ' + number, color = discord.Colour(0x0000FF),)
                embed.add_field(name="🏫 School Name", value=json_parsed["school_name"], inline=False)
                embed.add_field(name="📍 Location", value=f"{json_parsed['city']}, {json_parsed['state_prov']}, {json_parsed['country']}", inline=False)
                await message.channel.send(embed=embed)
            except ValueError:
                await message.channel.send("Invalid Team Number")
                
            

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(Token)
