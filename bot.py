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
            while True:

                pics = [
                    'https://cdn.discordapp.com/attachments/138194552837111808/715316841370878093/18f93d0d731738a77d9d00a6276110bd.png',
                    'https://cdn.discordapp.com/attachments/138194552837111808/715317021906042890/19592b6928c9774b0ba32ff3833eade2.png',
                    'https://cdn.discordapp.com/attachments/138194552837111808/715317267356975144/a09ed40d742442ef6083133428769c65.png',
                    'https://cdn.discordapp.com/attachments/138194552837111808/715317529337266357/41f11a46e7ed2e117bfe480b0296bdce.png',
                    'https://gfycat.com/agedfrayedcolt-twice-mina-kpop',
                    'https://cdn.discordapp.com/attachments/138194552837111808/715500100557865031/unknown.png',
                    'https://cdn.discordapp.com/attachments/138194552837111808/715438453822586920/hotwice-751444273703165952-20160708_235410-img4.jpg',
                    'https://cdn.discordapp.com/attachments/138194552837111808/715415435612258405/CzVT7pLUAAAcieq.jpg',
                    'https://gfycat.com/gratefulbreakablecricket']
                i = random.randint(0, len(pics) - 1)
                await message.channel.send('```Day ' + str(days) + '```')
                days += 1
                selected_pic = pics[i]
                await message.channel.send(selected_pic)
                if days == 27:
                    await message.channel.send('@Akhil, the images are done, need to add more')
                    break

                await asyncio.sleep(86400)
                pics.remove(selected_pic)



client = MyClient()
client.run('NTA0MzUwMTc2NjMxMDYyNTI5.XsC_Xg._Qr4IYSIIFbd4sBwdCPtf3OutVQ')
