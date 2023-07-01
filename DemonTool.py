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
{Fore.MAGENTA} _______                                            ________                    __ 
{Fore.LIGHTMAGENTA_EX}|       \                                          |        \                  |  
{Fore.MAGENTA}| $$$$$$$\  ______   ______ ____    ______   _______\$$$$$$$$______    ______  | $$
{Fore.LIGHTMAGENTA_EX}| $$  | $$ /      \ |      \    \  /      \ |       \ | $$  /      \  /      \ | $$
{Fore.LIGHTMAGENTA_EX}| $$  | $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\| $$$$$$$\| $$ |  $$$$$$\|  $$$$$$\| $$
{Fore.MAGENTA}| $$  | $$| $$    $$| $$ | $$ | $$| $$  | $$| $$  | $$| $$ | $$  | $$| $$  | $$| $$
{Fore.LIGHTMAGENTA_EX} $$__/ $$| $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$  | $$| $$ | $$__/ $$| $$__/ $$| $$
{Fore.MAGENTA}| $$    $$ \$$     \| $$ | $$ | $$ \$$    $$| $$  | $$| $$  \$$    $$ \$$    $$| $$
{Fore.LIGHTMAGENTA_EX} \$$$$$$$   \$$$$$$$ \$$  \$$  \$$  \$$$$$$  \$$   \$$ \$$   \$$$$$$   \$$$$$$  \$$

'''

Main_Hub = f"""
{Fore.CYAN}1 = PINGER       
{Fore.CYAN}2 = WEB SCRAPPER
{Fore.CYAN}3 = IP GEO    
{Fore.CYAN}4 = DISCORD NUKER
{Fore.CYAN}5 = GMAIL BRUTEFORCE
{Fore.CYAN}6 = NITRO GEN
{Fore.CYAN}7 = {Fore.RED}EXIT


"""


def clear_screen():
    # Clear screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear') 
print(Main_Logo)
userName = input(Fore.CYAN + " \n\nUsername: ")  #Ask's the User for Username input
password = input(Fore.CYAN + "Password: ") # Ask's the user for their password


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
        choice = input(Fore.CYAN + 'Enter a Number: ')
        if choice == '1':
            clear_screen()
            subprocess.call(['python', 'C:/Users/Nick/Desktop/DemonTool/Tools//ippinger.py'])
        elif choice == '2':
            clear_screen()
            s = input("Enter Website: ")
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
            print('Exiting')
            time.sleep(1)
            break
        else: 
            print(Colors.red + "Invalid Input!")
            time.sleep(1)
            continue



Main()
