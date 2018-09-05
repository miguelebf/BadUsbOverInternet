###############################
#                             #
#  Author: Miguel Bustamante  #
#  Server InternetDuck v 1.0  #
#                             #
###############################
import Funtions
import socket
import os
import sys

def main():
    file=None
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=9999
    host = socket.gethostname()
    try:
        #Detecta Sistema Operativo
        #--opertiveSystem = sys.platform
        # Bindea el puerto
        serversocket.bind((host, port))
        # Cola de hasta 1 peticiones 
        serversocket.listen(1)
        # Espera por el cliente 
        print("[+] Esperando conexion con BadUsbOverInternet...")
        clientsocket, addr = serversocket.accept()
        print("[+] Se ha establecido conexion con el BadUsbOverInternet")
        flag=True
        while flag:
            Funtions.showBanner()
            Funtions.showMenu()
            option=input("[?]Ingresa una opcion: ")
            if option=="1":  
                Funtions.moidifyScript()
            elif option=="2":
                Funtions.readScript(file)
            elif option=="3":
                Funtions.sendScript(clientsocket,file) 
            elif option=="4":
                file = open("Script.txt", "r")
                clientsocket.send(file.read().encode('ascii'))
                file.close()
            elif option=="5":
                flag=False
            else:
                print("[!]Seleccion incorrecta!")        
        
        clientsocket.close()
        print("[-]Adios!")
        sys.exit()
        #clientsocket.send(msg.encode('ascii'))
    except KeyboardInterrupt:
        try:
            clientsocket.close()
            file.close()
            print("[-]Adios!")
        except:
            print("[-]Adios!")
        sys.exit()

if (__name__ == "__main__"):
    main()
    
    
