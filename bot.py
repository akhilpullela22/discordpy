import discord
import random
import datetime
import os
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print(discord.__version__)





    async def on_message(self, message):
        if message.content == 'activate':
            channel = self.get_channel(707642477997195356)
            #week1
            pics = ['https://cdn.discordapp.com/attachments/713149370421477490/713150085151719514/190105_miraclenight324_2.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150081800470538/190105_miraclenight324_1.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150099928121414/190105_37minago_2.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150073533366322/1570161842-egan1fvwkaed8cv.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150023214301264/171030__LIKEY___2.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150018676326420/2019-03-24_28.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150016386105434/4theTWICE-1082972550534094848-20190109_200911-img3.jpg']
            i = random.randint(0, len(pics)-1)
            if pics[i] in pics:
                await channel.send(pics[i])
                pics.remove(pics[i])
            await asyncio.sleep(86400)






                








client = MyClient()
client.run('NTA0MzUwMTc2NjMxMDYyNTI5.XsC_Xg._Qr4IYSIIFbd4sBwdCPtf3OutVQ')