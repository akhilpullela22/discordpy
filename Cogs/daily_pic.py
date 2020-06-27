import discord
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class daily_pic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Data: Online')

    @commands.command(aliases = ['daily_pic'])
    async def daily_mina(self, ctx):
            days = 47
            i = 0
            
            pics = [
                'https://cdn.discordapp.com/attachments/138194552837111808/726165718084616273/ELz_lS_XsAEO4NA.png',
                'https://media.discordapp.net/attachments/138194552837111808/726289751073882182/20200627_121500.jpg?width=475&height=475',
                'https://cdn.discordapp.com/attachments/138194552837111808/726115878730727445/tumblr_p1gvkrW1xc1uacoejo1_1280.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/725837934078590986/f59850b6ed8210fb8b31730b9c8056cd.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/725824432051978301/image0.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/725614547842498590/image0.png',
                'https://lh3.googleusercontent.com/VL0eXw7n2qKk4i-KD6IA0UKdW7ExrQKhN7gLLSCPxt73emssHZn-Op83X81V5pvXMVNIB4qu99BqurasLSI5PT9DIKRRygVyvg=w1600-rj',
                'https://media.discordapp.net/attachments/138194552837111808/725151195655831553/181123_KBS_Music_Bank_2.jpg?width=296&height=474',]
            while True:
                await ctx.channel.send('```Day ' + str(days) + '```')
                days += 1
                selected_pic = pics[i]

                await ctx.channel.send(selected_pic)
                i += 1

                if days == 55:
                    break
                await asyncio.sleep(86400)
def setup(bot):
    bot.add_cog(daily_pic(bot))            