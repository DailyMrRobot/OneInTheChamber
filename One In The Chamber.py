import os
import random
import discord
import requests
import json
import youtube_dl
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord import client

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)





load_dotenv()
TOKEN = os.getenv('')

bot = commands.Bot(command_prefix='!')

@bot.command(name='rrve')
async def very_easy(ctx):
    VEasy_Mode = ["Miss","Miss","Jammed","Jammed","Miss","Hit"]
    response = random.choice(VEasy_Mode)
    await ctx.send(response)
@bot.command(name='rre')
async def russian_roulette(ctx):
    Easy_Mode = ["Miss","Miss","Miss","Miss","Hit","Hit"]
    response = random.choice(Easy_Mode)
    await ctx.send(response)
@bot.command(name='rrm')
async def medium_mode(ctx):
    Kinda_Mid = ["Miss","Miss","Miss","Hit","Hit","Hit"]
    response = random.choice(Kinda_Mid)
    await ctx.send(response)
@bot.command(name='rrh')
async def hard_on(ctx):
    Hard_Mode = ["Miss","Miss","Hit","Hit","Hit","Hit"]
    response = random.choice(Hard_Mode)
    await ctx.send(response)
@bot.command(name='rrvh')
async def Very_Hard(ctx):
    Rock_Hard = ["Miss","Hit","Hit","Hit","Hit","Hit"]
    response = random.choice(Rock_Hard)
    await ctx.send(response)


bot.run('')
