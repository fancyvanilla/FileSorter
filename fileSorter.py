#! /usr/bin/python3
import os
# import yaml
import json
from colorama import Fore
import platform

art = """ 
 ___  ____  ____  __  __  ____    ___  _   _  ____  ____  ____ 
/ __)( ___)(_  _)(  )(  )(  _ \  / __)( )_( )(_  _)( ___)(_  _)
\__ \ )__)   )(   )(__)(  )___/  \__ \ ) _ (  _)(_  )__)   )(  
(___/(____) (__) (______)(__)    (___/(_) (_)(____)(__)   (__) 
"""

def detectOs():
  system_name = platform.system()
  if system_name == "Linux":
    return "Linux"
  elif system_name == "Darwin":
    return "macOS" 
  elif system_name == "Windows":
    return "Windows"
  else:
    return None 


def valid_input():
    while True:
        try:
            option = int(input(":$ "))
            break
        except ValueError:
            print('Please type a valid option.')
    return option


def installer(config,os):
    packages = config[os]
    i = 1
    for p in packages:
        print('[', i, ']', p[0], '\n')
        i = i+1
    option = valid_input()
    if (option in range(1, len(packages)+1)):
        os.system(packages[option-1][1])
    else:
        print(Fore.YELLOW + "Pick a valid option\n")
    return None


def add(config,os):
    print(Fore.YELLOW + "What's the name of the automated command: ")
    pack_name = str(input(':$ '))
    print(Fore.YELLOW + "What's the command to run the command: ")
    pack_com = str(input(':$ '))
    pack = [pack_name, pack_com]
    config[os].append(pack)
    return config


def remove(config):
    packages = config[os]
    i = 1
    for p in packages:
        print('[', i, ']', p[0], '\n')
        i = i+1

    print(Fore.YELLOW + "What's the number of the command you want to delete: \n")
    option = valid_input()

    print(Fore.YELLOW + "Are you sure? y/n")
    confirm = str(input(':$ ')).upper().replace(" ", "")

    if confirm == "YES" or confirm == "Y" and option in range(1, len(packages)+1):
        packages.pop(option-1)
    elif (confirm == "NO" or confirm == "N"):
        print(Fore.YELLOW + "\nBack to the main menu\n")
    else:
        print(Fore.YELLOW + "\nPick a valid option\n")
    return config


def main():
    with open('config.json', 'r') as file:
        config = json.load(file)
    with open('config.json', 'w') as file:
        json.dump(config, file)
    while True:
        print(art)
        print(
            Fore.CYAN + "[!] The idea by: @elfalehdev and shoutout to @cryptolake for the update.\n")
        print(
            Fore.RED + "[1] Install packages \n[2] Add a package to the config\n[3] Remove a package from the config\n[4] Exit")
        option = valid_input()
        os=detectOs()
        if not os:
            print(Fore.BLACK+"[!!] Unknown or Unsupported operating system !")
        if (option == 1):
            installer(config,os)
        elif (option == 2):
            config = add(config,os)
        elif (option == 3):
            config = remove(config,os)
        elif (option == 4):
            exit()
        else:
            print('Please choose an appropriate option.\n')
              

if __name__ == '__main__':
    main()

