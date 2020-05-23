import discord
import random
import datetime

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print(discord.__version__)



    async def on_message(self, message):
        # don't respond to the bot user
        if message.author == self.user:
            return

        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        print(hour)
        if hour == '00' and minute == '02':
            channel = client.get_channel(713149370421477490)
            pics = ['https://cdn.discordapp.com/attachments/713149370421477490/713150013437378581/4dad2710138b944728716782e88b3ccc.jpg','https://cdn.discordapp.com/attachments/713149370421477490/713150023214301264/171030__LIKEY___2.jpg','https://cdn.discordapp.com/attachments/713149370421477490/713150073533366322/1570161842-egan1fvwkaed8cv.jpg','https://media.discordapp.net/attachments/713149370421477490/713150085151719514/190105_miraclenight324_2.jpg?width=1016&height=677', 'https://cdn.discordapp.com/attachments/713149370421477490/713150099928121414/190105_37minago_2.jpg', 'https://cdn.discordapp.com/attachments/713149370421477490/713150074426884147/569437_243451_329_org.jpg']
            i = random.randrange(len(pics))
            selected = pics[i]
            await channel.message.send(selected)
                








client = MyClient()
client.run('NTA0MzUwMTc2NjMxMDYyNTI5.XsC_Xg._Qr4IYSIIFbd4sBwdCPtf3OutVQ')