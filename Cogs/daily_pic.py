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
            days = 50
            i = 0
            
            pics = [
                'https://cdn.discordapp.com/attachments/138194552837111808/726895341026279524/wnaxecfrdc131.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/726934631940751401/dreamnara0324-972965310419496960-20180312_063941-img1.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/727026524527525938/EKpkPdVUYAA7rCo.png',
                'https://cdn.discordapp.com/attachments/138194552837111808/726824222193614929/TWICELIGHTS_in_JAPAN_Red_Postcards_SCANS_3.jpeg',
                'https://cdn.discordapp.com/attachments/138194552837111808/726758490856489060/20200627_143101.jpg',
                'https://cdn.discordapp.com/attachments/138194552837111808/726590783527977040/llw7tukqwgn11.jpg',
                'https://images-ext-1.discordapp.net/external/R08yiMfa3Pe3BQdxWgdtRDNVjt0BIXTfy_5NqswWXh8/https/pbs.twimg.com/media/EazcK-WU8AAJYSj.jpg%3Alarge?width=845&height=475',
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

                if days == 63:
                    break
                await asyncio.sleep(86400)
def setup(bot):
    bot.add_cog(daily_pic(bot))            