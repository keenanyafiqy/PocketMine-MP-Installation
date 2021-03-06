#!/usr/bin/python3
import os
import time
import sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

def clear():
    if os.name == 'posix':
        _ = os.system("clear")
    else:
        _ = os.system("cls")

clear()

slowprint("Starting the setup...")
clear()

slowprint("Welcome to PocketMine-MP Installation (64-bit) - Android")
slowprint("Copyright 2022 KeenTeams - PocketMine-Setup v1.0.1")
print(" ")
slowprint("-------------------------------------")
print(" ")
slowprint("Created by Keenan Yafiq (keenanyafiqy)")
slowprint("Executed from Python")
slowprint("This installation will install PocketMine-MP v4.x.x")
print(" ")
slowprint("Sometimes package cannot be downloaded automatically because the package cannot be located or user storage is full, so you may needed fast internet connection and empty storages")
print(" ")
slowprint("-------------------------------------")
print(" ")
choice = input("Do you want to start the installation? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("You will install:")
slowprint("1. make")
slowprint("2. autoconf")
slowprint("3. automake")
slowprint("4. libtool")
slowprint("5. m4")
slowprint("6. wget")
slowprint("7. getconf")
slowprint("8. gzip")
slowprint("9. bzip2")
slowprint("10. bison")
slowprint("11. g+ or g++")
slowprint("12. git")
slowprint("13. cmake")
slowprint("14. pkg-config")
slowprint("15. re2c")
print(" ")

choice = input("Start the setup? (Typing 'n' will cancel the setup!) [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("Starting setup...")
slowprint("Installing 15 packages...")
os.system ("pkg install make")
os.system ("pkg install autoconf")
os.system ("pkg install automake")
os.system ("pkg install libtool")
os.system ("pkg install m4")
os.system ("pkg install wget")
os.system ("pkg install getconf")
os.system ("pkg install gzip")
os.system ("pkg install bzip2")
os.system ("pkg install bison")
choice = input("Package g+ or g++ cannot be located, do you want to try it out? [y/n]: ")
if choice == 'n' : slowprint("1 packages installation has been cancelled")
if choice == 'y' : os.system ("pkg install g++")
os.system ("pkg install git")
os.system ("pkg install cmake")
os.system ("pkg install pkg-config")
os.system ("pkg install re2c")
clear()

choice = input("All/Some required packages are ready. Do you want to install source PocketMine-MP? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("Installing PocketMine-MP....")
slowprint("Creating folder 'Server'...")
os.system("mkdir Server")
os.system("cd Server")
slowprint("Getting all files from https://get.pmmp.io...")
os.system ("wget -q -O - https://get.pmmp.io | bash -s -")
slowprint("Successfully completed the setup. Type './start.sh' to start the server")
slowprint("This setup cannot start with rooted user.")
choice = input("Exit? The setup succesfully completed. [y]")
if choice == 'y' : sys.exit()
sys.exit()