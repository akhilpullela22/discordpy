import discord
import random
import datetime
import os
import asyncio
from bs4 import BeautifulSoup
from googletrans import Translator
import requests



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print(discord.__version__)

    async def on_message(self, message):
        if  message.content == 'cleanse':
            channel = client.get_channel
            await message.channel.purge(limit=150)
            await message.channel.send('this channel has been cleansed')
        
        

        
        if message.content == 'daily-mina':
            days = 34
            i = 0
            channel = client.get_channel(713149370421477490)
            pics = [
                'https://cdn.discordapp.com/attachments/138194552837111808/721477905263362170/unknown.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/721520040142176316/DooDoo_22-838105251429277696-20170305_031357-img1.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/721520250453229638/DooDoo_22-838265101132021764-20170305_134908-img1.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/721477402378764399/tumblr_ojtu340bTY1uacoejo1_1280.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/721477447199096852/C-FD8meVoAM9DNd.png',
                'https://pbs.twimg.com/media/EaWBcCFUMAAwrJe.jpg:large',
                'https://cdn.discordapp.com/attachments/138194552837111808/721380342837018694/478427e99bb7f14316f23ac957509a66.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/721309352895709215/e99a2a9e50ff6e0ec58a6c55d9b5d25f.png',]
            while True:
                await message.channel.send('```Day ' + str(days) + '```')
                days += 1
                selected_pic = pics[i]

                await message.channel.send(selected_pic)
                i += 1

                if days == 41:
                    await message.channel.send('akhil, you pabo, we are on day 40 you need to add more images!')
                    break
                await asyncio.sleep(86400)
        if message.content == 'word':
            url = 'https://www.koreanclass101.com/korean-phrases/'
            channel = client.get_channel(719070843287896117)
            while True:
                source = requests.get(url).text
                soup = BeautifulSoup(source, 'lxml')
                word = soup.find('div', class_= 'r101-wotd-widget__word' ).text
                romanization = soup.find('div', class_= 'r101-wotd-widget__additional-field romanization' ).text
                translator = Translator()
                translation1 = translator.translate(word, dest = 'te').text 
                translation2 = translator.translate(word, dest = 'en').text
                await message.channel.send('KOREAN WORD OF THE DAY:')
                await message.channel.send(word + ': ' +romanization)
                await message.channel.send('English TRANSLATION: '+translation2)
                await message.channel.send('Telugu TRANSLATION: ' +translation1)    
                await asyncio.sleep(86400)        


        
      


client = MyClient()
client.run('NTA0MzUwMTc2NjMxMDYyNTI5.XsC_Xg._Qr4IYSIIFbd4sBwdCPtf3OutVQ')
