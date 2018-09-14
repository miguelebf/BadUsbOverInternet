###############################
#                             #
#  Author: Miguel Bustamante  #
#  Server WBU v 0.1           #
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
        opertiveSystem = sys.platform
        # Bindea el puerto
        serversocket.bind((host, port))
        # Cola de hasta 1 peticiones 
        serversocket.listen(1)
        # Espera por el cliente 
        print("[+] Waiting connection with BadUsb...")
        clientsocket, addr = serversocket.accept()
        print("[+]Connection has been established with BadUsb")
        flag=True
        while flag:
            Funtions.showBanner()
            Funtions.showMenu()
            option=input("[?]Please enter an option: ")
            if option=="1":  
                Funtions.moidifyScript(opertiveSystem)
            elif option=="2":
                Funtions.readScript(file)
            elif option=="3":
                Funtions.sendScript(clientsocket,file) 
            elif option=="4":
                print("Developing..")
            elif option=="5":
                flag=False
            else:
                print("[!]Incorrect selection!")        
        
        clientsocket.close()
        print("[-]Bye!")
        sys.exit()
    except KeyboardInterrupt:
        try:
            clientsocket.close()
            file.close()
            print("[-]Bye!")
        except:
            print("[-]Bye!")
        sys.exit()

if (__name__ == "__main__"):
    main()
    
    
