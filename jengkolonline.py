#coding=utf-8
import os,sys
pkg update && pkg upgrade
pkg install git
pkg install python
pkg install python2
pkg install python3
pip2 install requests
pip2 install bs4
print ("install tools selesai...")
def menu():
print("""_ _____ _   _  ____ _  _____  _        ___  _   _ _     ___ _   _ _____
      | | ____| \ | |/ ___| |/ / _ \| |      / _ \| \ | | |   |_ _| \ | | ____|
   _  | |  _| |  \| | |  _| ' / | | | |     | | | |  \| | |    | ||  \| |  _|
  | |_| | |___| |\  | |_| | . \ |_| | |___  | |_| | |\  | |___ | || |\  | |___
   \___/|_____|_| \_|\____|_|\_\___/|_____|  \___/|_| \_|_____|___|_| \_|_____|
 1. ENC & DEC HASH
 2.
 3.
 4.
 5.
 6.
 7.
 8.
 9.
 10.
 """)
 
 menu()
  pilih =raw_input("[©]nomor:")
  if pilih =="":
    print "Pilih Yg Benner Woy"
    exit()
  if pilih =="1":
    os.system("clear")
    print ("Tunggu sebentar...")
    os.system("")
    os.system("python2  ")
    
    
