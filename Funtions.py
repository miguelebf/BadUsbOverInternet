#Imports 
import socket
import os
import random
def showBanner():
    strBanner1="""
    
 ____            _ _    _     _   
|  _ \          | | |  | |   | |    
| |_) | __ _  __| | |  | |___| |__  
|  _ < / _` |/ _` | |  | / __| '_ \ 
| |_) | (_| | (_| | |__| \__ \ |_) |
|____/ \__,_|\__,_|\____/|___/_.__/                                               
         ____                   _____       _                       _   
        / __ \                 |_   _|     | |                     | |  
       | |  | |_   _____ _ __    | |  _ __ | |_ ___ _ __ _ __   ___| |_ 
       | |  | \ \ / / _ \ '__|   | | | '_ \| __/ _ \ '__| '_ \ / _ \ __|
       | |__| |\ V /  __/ |     _| |_| | | | ||  __/ |  | | | |  __/ |_ 
        \____/  \_/ \___|_|    |_____|_| |_|\__\___|_|  |_| |_|\___|\__|       
v0.1 by Miguel Bustamante
    """
    strBanner2="""
888       888 888888b.        888     888 
888   o   888 888  "88b       888     888 
888  d8b  888 888  .88P       888     888 
888 d888b 888 8888888K.       888     888 
888d88888b888 888  "Y88b      888     888 
88888P Y88888 888    888      888     888 
8888P   Y8888 888   d88P      Y88b. .d88P 
888P     Y888 8888888P" AD     "Y88888P" SB 
    
       
v0.1 by Miguel Bustamante
    """
    strBanner3="""

01010111 01000010 01010101

v0.1 by Miguel Bustamante
    """
    num=random.randint(1, 2)
    if num==1:
        print(strBanner1)
    elif num ==2:
        print(strBanner2)
    else:
        print(strBanner3)

    return 

def showMenu():
    strMenu="""
        1. Modify Script
        2. Show Script
        3. Send Script
        4. Interactive Mode            
        5. Exit
    """
    print(strMenu)
    return 
def readScript(file):
    file = open("Script.txt", "r")
    print("--------------------------------------------")
    print(file.read())
    print("--------------------------------------------")
    input("[?]Enter to continue..")
    file.close()
    return

def sendScript(clientsocket,file):
    file = open("Script.txt", "r")
    clientsocket.send(file.read().encode('ascii'))
    print("[+]Sent Script")
    print("[+]Running Script ...")
    respuesta=clientsocket.recv(1024)
    
    if (respuesta.decode()=="1"):
        print("[+]Executed Script")
    else:
        print("[!]Error")
        input("[?]Enter to continue..")
        return
    input("[?]Enter to continue..")
    
    return

def moidifyScript(operativeSystem):
    print("/n"+"[+]Modify Script & Save it!...")
    
    if operativeSystem=="linux2":
        os.system('nano Script.txt')
    elif operativeSystem=="darwin":
        os.system('open -t Script.txt')
    elif operativeSystem=="win32" or operativeSystem=="win64":
        os.system('notepad Script.txt')
    else:
        print("[!]Unknown Operative System")
    
    input("[?]Enter to continue..")
    return
