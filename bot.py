import discord
import random
import datetime
import os
import asyncio
from periodic import Periodic


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print(discord.__version__)

    async def on_message(self, message):
        if message.content == 'daily-mina':
            days = 18
            channel = client.get_channel(713149370421477490)
            pics = [
                'https://cdn.discordapp.com/attachments/138194552837111808/715316841370878093/18f93d0d731738a77d9d00a6276110bd.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/715317021906042890/19592b6928c9774b0ba32ff3833eade2.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/715317267356975144/a09ed40d742442ef6083133428769c65.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/715317529337266357/41f11a46e7ed2e117bfe480b0296bdce.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/715317341755277335/0f9791b7521bc060f83e9f7f4c6ab4fc.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/715500100557865031/unknown.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/715438453822586920/hotwice-751444273703165952-20160708_235410-img4.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/715415435612258405/CzVT7pLUAAAcieq.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/715762678370402394/EZJ1nxFVAAAKNEU.png'
                'https://pbs.twimg.com/media/EZJ2CvSU0AAleIj.jpg:orig'
                'https://cdn.discordapp.com/attachments/138194552837111808/715505094338019369/TTV5_Mina25.jpg'
                'https://images-ext-1.discordapp.net/external/FG7Wwd0FgpGWhAfplwORBAWcuTY5p1E9dA_S40MvIvo/https/pbs.twimg.com/media/CzyYkQ7UsAAMhfF.jpg%3Alarge?width=1016&height=677'
                'https://media.discordapp.net/attachments/138194552837111808/715317316186931250/05093fc8406dd0b48e31a5e4313b98bf.png?width=508&height=677'
                'https://images-ext-1.discordapp.net/external/3RTnAteR8-SR9VxHWTs-_1pInFbzrOKcw3xq28cozF8/https/pbs.twimg.com/media/EYcFjcWUMAUeUWo.jpg%3Aorig?width=451&height=677'
                'https://pbs.twimg.com/media/EYY7OJEU0AAyjfF.jpg:orig'
                'https://pbs.twimg.com/media/EYY7OJLVcAAqT4D.jpg:orig'
                'https://gfycat.com/fancyimaginarybuzzard']
            while True:
                i = random.randint(0, len(pics)-1)
                await message.channel.send('```Day ' + str(days) + '```')
                days += 1
                selected_pic = pics[i]
                await message.channel.send(selected_pic)
                pics.remove(selected_pic)
                if len(pics) == 0:
                    await message.channel.send('@Akhil, the images are done, need to add more')
                    break

                await asyncio.sleep(1)




client = MyClient()
client.run('NTA0MzUwMTc2NjMxMDYyNTI5.XsC_Xg._Qr4IYSIIFbd4sBwdCPtf3OutVQ')
