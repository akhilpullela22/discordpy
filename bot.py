import discord
import random
import datetime
import os
import asyncio
#from bs4 import BeautifulSoup
#from googletrans import Translator
import requests
from discord.ext import commands
from collections import defaultdict


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
        
        if '!help' in message.content:
            await message.channel.send("!team + number for general information regarding a team \n !awards + number for award history of a team \n !events + team + year for events data for teams during a specific year")
        if '!team' in message.content:
            parts = message.content.split(" ", 1)
            if len(parts) > 1:
                number = parts[1]
            try:
                int(number)
                response = requests.get(f"https://www.thebluealliance.com/api/v3/team/frc{number}",
                headers={
                "X-TBA-Auth-Key": auth_key}
                )
                json_parsed = response.json()
                embed = discord.Embed(title = 'Team ' + number, color = discord.Colour(0x0000FF),description=json_parsed["nickname"])
                embed.add_field(name="🏫 **School**", value=json_parsed["school_name"], inline=False)
                embed.add_field(name="📍 **Location**", value=f"{json_parsed['city']}, {json_parsed['state_prov']}, {json_parsed['country']}", inline=False)
                embed.add_field(name="🎯 **Established**", value=str(json_parsed["rookie_year"]), inline=False)
                embed.set_footer(text="Data provided by The Blue Alliance")
                embed.timestamp = discord.utils.utcnow()
                await message.channel.send(embed=embed)
            except ValueError:
                await message.channel.send("Invalid Team Number")
        if '!awards' in message.content:
            parts = message.content.split(" ", 1)
            if len(parts) > 1:
                number = parts[1]
            response = requests.get(f"https://www.thebluealliance.com/api/v3/team/frc{number}/history",
                headers={
                "X-TBA-Auth-Key": auth_key}
                )
            json_parsed = response.json()
            awards_by_name = defaultdict(list)
            for award in json_parsed["awards"]:
                awards_by_name[award["name"]].append(str(award["year"]))


            for award_name, years in awards_by_name.items():
                embed = discord.Embed(
                    title=f'Award: {award_name}', 
                    color=discord.Colour(0x0000FF), 
                    description=f'Years: {", ".join(years)}'
                )
                embed.set_footer(text="Data provided by The Blue Alliance")
                embed.timestamp = discord.utils.utcnow()
                await message.channel.send(embed=embed)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(Token)
