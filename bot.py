import discord
import random
import datetime
import os
import asyncio
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
from discord.ext import commands

Token = 'NTA0MzUwMTc2NjMxMDYyNTI5.XvbdkA.rK2Uo0v_bwcgvswFrQQBq-NGy0E'

bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')
         
@bot.event
async def on_ready():
    print('Status: Online') 
    activity = discord.Activity(name = 'TWICE', type = discord.ActivityType.listening)
    return await bot.change_presence(activity = activity)

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

        
      



bot.run(Token)
