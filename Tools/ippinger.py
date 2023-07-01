import os
from time import localtime, strftime, sleep
import colorama
import smtplib, sys
import requests
import socket
from PIL import ImageGrab
from gtts import gTTS
from scapy.all import *
from pystyle import Colors
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)
import subprocess

def print_logo():
    logo = '''
        _______                                               ______  _______  
        |       \                                             |      \|       \ 
        | $$$$$$$\  ______   ______ ____    ______   _______   \$$$$$$| $$$$$$$\
        | $$  | $$ /      \ |      \    \  /      \ |       \   | $$  | $$__/ $$
        | $$  | $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\| $$$$$$$\  | $$  | $$    $$
        | $$  | $$| $$    $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$  | $$$$$$$ 
        | $$__/ $$| $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$  | $$ _| $$_ | $$      
        | $$    $$ \$$     \| $$ | $$ | $$ \$$    $$| $$  | $$|   $$ \| $$      
        \$$$$$$$   \$$$$$$$ \$$  \$$  \$$  \$$$$$$  \$$   \$$ \$$$$$$ \$$ 
    '''
    print(Fore.LIGHTMAGENTA_EX + Fore.MAGENTA + logo + Style.RESET_ALL)

def ippinger():
    ip = input('Enter IP: ')
    ping_process = subprocess.Popen(['ping', ip])
    ping_process.wait()  # Wait for the ping process to finish
    Main()

print_logo()
ippinger()

    