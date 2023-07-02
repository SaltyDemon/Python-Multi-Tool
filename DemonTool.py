import os
from time import localtime, strftime, sleep
import colorama
import smtplib, sys
import requests
import socket
import string
from PIL import ImageGrab
from gtts import gTTS
from scapy.all import *
from pystyle import Colors
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import subprocess


Main_Logo = f'''
{Fore.MAGENTA}______                         _____           _ 
{Fore.LIGHTMAGENTA_EX}|  _  \                       |_   _|         | |
{Fore.MAGENTA} | | |___ _ __ ___   ___  _ __ | | ___   ___ | |
{Fore.LIGHTMAGENTA_EX}| | | / _ \ '_ ` _ \ / _ \| '_ \| |/ _ \ / _ \| |
{Fore.MAGENTA}| |/ /  __/ | | | | | (_) | | | | | (_) | (_) | |
{Fore.MAGENTA}|___/ \___|_| |_| |_|\___/|_| |_\_/\___/ \___/|_|
                                                 

'''

Main_Hub = f"""
{Fore.WHITE}╔══════════════════════╗
{Fore.WHITE}║ {Fore.MAGENTA}[1]{Fore.WHITE}= {Fore.LIGHTMAGENTA_EX}PINGER          {Fore.WHITE}║       
{Fore.WHITE}║ {Fore.MAGENTA}[2]{Fore.WHITE}= {Fore.LIGHTMAGENTA_EX}WEB SCRAPPER    {Fore.WHITE}║       
{Fore.WHITE}║ {Fore.MAGENTA}[3]{Fore.WHITE}= {Fore.LIGHTMAGENTA_EX}IP GEO          {Fore.WHITE}║       
{Fore.WHITE}║ {Fore.MAGENTA}[4]{Fore.WHITE}= {Fore.LIGHTMAGENTA_EX}DISCORD NUKER   {Fore.WHITE}║        
{Fore.WHITE}║ {Fore.MAGENTA}[5]{Fore.WHITE}= {Fore.LIGHTMAGENTA_EX}GMAIL BRUTEFORCE{Fore.WHITE}║       
{Fore.WHITE}║ {Fore.MAGENTA}[6]{Fore.WHITE}= {Fore.LIGHTMAGENTA_EX}NITRO GEN       {Fore.WHITE}║       
{Fore.WHITE}║ {Fore.MAGENTA}[7]{Fore.WHITE}= {Fore.RED}EXIT            {Fore.WHITE}║                                                                                    
{Fore.WHITE}╚══════════════════════╝
                                                                               




"""


def clear_screen():
    # Clear screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear') 
print(Main_Logo)
userName = input(Fore.LIGHTMAGENTA_EX + " \n\nUsername: ")  #Ask's the User for Username input
password = input(Fore.LIGHTMAGENTA_EX + "Password: ") # Ask's the user for their password


count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.


while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.


    if count == 3: # Counter, to make sure the user only gets a limited number (3)of attempts
        print("\nThree Username and Password Attempts used. Goodbye") # Lets the user know they have reached their limit
        break # Leave the Loop and the whole program


    elif userName == 'Demon' and password == 'root@DemonTool': # The userName and password is equal to 'elmo' and 'blue', which is correct, they can enter FaceSnap!
        print("Welcome! ") # Welcomes the User, the username and password is correct
        break # Leave the loop and the whole program as the username and passowrd is correct


    elif userName != 'Demon' and password != 'root@DemonTool': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!") # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet
        
        
def Main():
    clear_screen()
    print(Main_Logo)
    print(Main_Hub)
    while True:
        choice = input(Fore.MAGENTA + 'Enter a Number: ')
        if choice == '1':
            clear_screen()
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools//ippinger.py'])
        elif choice == '2':
            clear_screen()
            s = input(Fore.MAGENTA + "Enter Website: ")
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools/webscrapper.py'])
            print(Colors.red + "YOU HAVE 60 SECONDS TO GATHER INFORMATION")
            time.sleep(1000)
            Main()
        elif choice == '3':
            clear_screen()
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools/ipgeo.py'])
            print(Colors.red + "YOU HAVE 15 SECONDS TO GATHER INFORMATION")
            print(Colors.red + "YOU HAVE 15 SECONDS TO GATHER INFORMATION")
            print(Colors.red + "YOU HAVE 15 SECONDS TO GATHER INFORMATION")
            time.sleep(15)
            Main()
        elif choice == '4':
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools/discordnuker.py'])
        elif choice == '5':
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools/gmailbruteforce.py'])
        elif choice == '6':
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools/nitrogen.py'])
        elif choice == '7':
            print(Fore.MAGENTA + 'Exiting')
            time.sleep(1)
            break
        else: 
            print(Colors.red + "Invalid Input!")
            time.sleep(1)
            continue



Main()
