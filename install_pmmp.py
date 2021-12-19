#!/usr/bin/python3
import os
import time
import sys

os.system ("clear")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint("Starting the setup...")
os.system ("clear")

slowprint("Welcome to PocketMine-MP Installation (64-bit)")
slowprint("Copyright 2021 KeenGames - PocketMine-Setup v1.2")
print(" ")
slowprint("-------------------------------------")
print(" ")
slowprint("Created by Keenan Yafiq (keenanyafiqy)")
slowprint("Executed from Python")
slowprint("This installation will install PocketMine-MP v3.25.2")
print(" ")
slowprint("Sometimes packages cannot be downloaded automatically because the packages cannot be located or they're storage is full, so you may needed fast internet connection and many storages")
print(" ")
slowprint("-------------------------------------")
print(" ")
choice = input("Do you want to start the installation? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("clear")

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
slowprint("Final Installation, you will be:")
slowprint("Installing the basics packages from Termux")
slowprint("Use the commands that has been listed on README.md to start install the basics packages")
print(" ")

choice = input("Start and continue the setup? (Typing 'n' will cancel the setup!) [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("clear")

slowprint("Starting to install 15 packages...")
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
os.system ("clear")

choice = input("Some packages has been installed, some packages cannot be installed, do you want to install source PocketMine-MP? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("clear")

slowprint("Starting the downloads....")
slowprint("Getting all files from https://get.pmmp.io...")
os.system ("wget -q -O - https://get.pmmp.io | bash -s -")
slowprint("Successfully completed the setup. Type './start.sh' to start the server")
slowprint("If you want to recompile the PHP, Type './compile.sh' to recompile the PHP")
slowprint("Make sure your devices is 64-bit and not rooted if you are so sure to install this software. Many peoples cannot install PocketMine-MP because they only have 32-bit systems")
slowprint("This setup cannot start with rooted user.")
print(" ")
choice = input("Start install Basics Termux packages? [y/n]: ")
if choice == 'n' : os.system ("clear")
if choice == 'y' : os.system ("git clone https://github.com/vpphacker/vppbasic")
os.system ("clear")
slowprint("Quitting the setup...")
sys.exit()
