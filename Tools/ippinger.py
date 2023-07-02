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
______                          ___________ 
|  _  \                        |_   _| ___ \
| | | |___ _ __ ___   ___  _ __  | | | |_/ /
| | | / _ \ '_ ` _ \ / _ \| '_ \ | | |  __/ 
| |/ /  __/ | | | | | (_) | | | || |_| |    
|___/ \___|_| |_| |_|\___/|_| |_\___/\_|
    '''
    print(Fore.LIGHTMAGENTA_EX + Fore.MAGENTA + logo + Style.RESET_ALL)

def ippinger():
    ip = input('Enter IP: ')
    ping_process = subprocess.Popen(['ping', ip])
    ping_process.wait()  # Wait for the ping process to finish
    Main()

print_logo()
ippinger()

    
