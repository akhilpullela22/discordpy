import discord
import random
import datetime
import os
import asyncio
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
from discord.ext import commands


class happy_bday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['hbd'])
    async def bday (self, ctx):
        embed = discord.Embed(title = 'HAPPY BIRTHDAY', color = discord.Colour(0xefe61),description = 'Mina wishes you HAPPY BIRTHDAY!',)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/713149370421477490/727027989564358725/ezgif.com-video-to-gif.gif')
        embed.set_footer(text = 'PenguinBot')           
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(happy_bday(bot))
        