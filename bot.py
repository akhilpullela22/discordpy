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
        if message.content == 'test':
            while message.content != 'stop':
                await message.channel.send('`periodic`')
                await asyncio.sleep(1)







                








client = MyClient()
client.run('NTA0MzUwMTc2NjMxMDYyNTI5.XsC_Xg._Qr4IYSIIFbd4sBwdCPtf3OutVQ')