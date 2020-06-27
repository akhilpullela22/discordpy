import discord
import random
import datetime
import os
import asyncio
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
from discord.ext import commands


class daily_word(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Data: Online')
    @commands.command (aliases=['word'])
    async def word (self, ctx):
            url = 'https://www.koreanclass101.com/korean-phrases/'
            while True:
                source = requests.get(url).text
                soup = BeautifulSoup(source, 'lxml')
                word = soup.find('div', class_= 'r101-wotd-widget__word' ).text
                romanization = soup.find('div', class_= 'r101-wotd-widget__additional-field romanization' ).text
                translator = Translator()
                translation1 = translator.translate(word, dest = 'te').text 
                translation2 = translator.translate(word, dest = 'en').text
                await ctx.send('KOREAN WORD OF THE DAY:')
                await ctx.send(word + ': ' +romanization)
                await ctx.send('English TRANSLATION: '+translation2)
                await ctx.send('Telugu TRANSLATION: ' +translation1)    
                await asyncio.sleep(86400)
def setup(bot):
    bot.add_cog(daily_word(bot))