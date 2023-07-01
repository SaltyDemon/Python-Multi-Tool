import requests
import os
from time import localtime, strftime, sleep
import colorama
import smtplib
import sys
import socket
from PIL import ImageGrab
import discord
from discord.ext import commands
from gtts import gTTS
from scapy.all import *
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def print_logo():
    logo = '''
        _______                                               ______  _______  
        |       \                                             |      \|       \ 
        | $$$$$$$\  ______   ______ ____    ______   _______   \$$$$$$| $$$$$$$
        | $$  | $$ /      \ |      \    \  /      \ |       \   | $$  | $$__/ $$
        | $$  | $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\| $$$$$$$\  | $$  | $$    $$
        | $$  | $$| $$    $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$  | $$$$$$$ 
        | $$__/ $$| $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$  | $$ _| $$_ | $$      
        $$    $$ \$$     \| $$ | $$ | $$ \$$    $$| $$  | $$|   $$ \| $$      
        \$$$$$$$   \$$$$$$$ \$$  \$$  \$$  \$$$$$$  \$$   \$$ \$$$$$$ \$$ 
    '''
    print(Fore.MAGENTA + Fore.LIGHTMAGENTA_EX + logo + Style.RESET_ALL)


def geolocation():
    ip_address = input("Enter the IP address: ")
    url = f"https://ipapi.co/{ip_address}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country = data.get('country_name')
        region = data.get('region')
        city = data.get('city')
        postal_code = data.get('postal')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(f"IP: {ip_address}")
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"Postal Code: {postal_code}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Unable to locate IP address.")


print_logo()
geolocation()
