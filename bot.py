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
            days = 27
            i = 0
            channel = client.get_channel(713149370421477490)
            pics = [
                'https://pbs.twimg.com/media/EZJ2CvSU0AAleIj.jpg:orig',
                'https://cdn.discordapp.com/attachments/138194552837111808/715505094338019369/TTV5_Mina25.jpg',
                'https://images-ext-1.discordapp.net/external/FG7Wwd0FgpGWhAfplwORBAWcuTY5p1E9dA_S40MvIvo/https/pbs.twimg.com/media/CzyYkQ7UsAAMhfF.jpg%3Alarge?width=1016&height=677',
                'https://media.discordapp.net/attachments/138194552837111808/715317316186931250/05093fc8406dd0b48e31a5e4313b98bf.png?width=508&height=677',
                'https://images-ext-1.discordapp.net/external/3RTnAteR8-SR9VxHWTs-_1pInFbzrOKcw3xq28cozF8/https/pbs.twimg.com/media/EYcFjcWUMAUeUWo.jpg%3Aorig?width=451&height=677',
                'https://pbs.twimg.com/media/EYY7OJEU0AAyjfF.jpg:orig',
                'https://pbs.twimg.com/media/EYY7OJLVcAAqT4D.jpg:orig',
                'https://gfycat.com/fancyimaginarybuzzard',]
            while True:
                await message.channel.send('```Day ' + str(days) + '```')
                days += 1
                selected_pic = pics[i]

                await message.channel.send(selected_pic)
                i += 1

                if days == 34:
                    await message.channel.send('akhil, you pabo, we are on day 35 you need to add more images!')
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
client.run(token)
