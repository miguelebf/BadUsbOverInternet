#Imports 
import socket
import os
def showBanner():
    strBanner="""
    
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
v1.0 by Miguel Bustamante
    """
    print(strBanner)
    return 

def showMenu():
    strMenu="""
        1. Modificar Script
        2. Ver Script
        3. Enviar Script
        4. Modo Interactivo            
        5. Salir
    """
    print(strMenu)
    return 
def readScript(file):
    file = open("Script.txt", "r")
    print("--------------------------------------------")
    print(file.read())
    print("--------------------------------------------")
    input("[?]Enter para continuar..")
    file.close()
    return

def sendScript(clientsocket,file):
    file = open("Script.txt", "r")
    clientsocket.send(file.read().encode('ascii'))
    print("[+]Envianado...")
    """respuesta=clientsocket.recv(1024)
    if (respuesta=="O"):
        print("[+]Script recibido por el BadUsb")
    else:
        print("[!]Error al enviar el script")
        input("[?]Enter para continuar..")
        return
    input("[?]Enter para continuar..")
    """
    return

def moidifyScript():
    print("/n"+"[+]Modifica el Script y Guardalo!...")
    os.system('gedit script.txt')    
    input("[?]Enter para continuar..")
    return
