import discord
import random
import datetime
import os
import asyncio
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
from discord.ext import commands


class icons_avatars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases = ['Ping', 'pong', 'Pong'])
    async def ping(self, ctx):
        await ctx.send(f':round_pushpin: {round(self.bot.latency * 1000)}ms! :round_pushpin:')

    
    @commands.command(aliases = ['Servericon', 'server_icon', 'Server_icon'])
    async def servericon(self, ctx):
        await ctx.send(ctx.guild.icon_url)

    
    @commands.command(aliases = ['Avatar', 'av', 'Av', 'dp', 'Dp', 'pfp', 'Pfp'])
    async def avatar(self, ctx, *, member : discord.Member = None):
        if member is None:

            embed1 = discord.Embed()
            embed1.colour = 0xefe61
            embed1.set_author(name = 'Avatar', icon_url = f'{ctx.author.avatar_url}')
            embed1.set_image(url = ctx.author.avatar_url)
            embed1.set_footer(text = 'PenguinBot()')
            embed1.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed = embed1)
        else:

            embed2 = discord.Embed()
            embed2.colour = 0xefe61
            embed2.set_author(name = f"{member.name}'s Avatar", icon_url = f'{member.avatar_url}')
            embed2.set_image(url = member.avatar_url)
            embed2.set_footer(text = 'PenguinBot')
            embed2.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed = embed2)    
def setup(bot):
    bot.add_cog(icons_avatars(bot))