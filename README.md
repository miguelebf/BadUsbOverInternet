# WBU
![Supported Python versions](https://img.shields.io/badge/python-3.6-orange.svg)  ![Supported OS](https://img.shields.io/badge/Supported%20OS-Kali_Linux-yellow.svg)  ![Conference](https://img.shields.io/badge/DragonJarCon-Colombia_2018-g.svg) ![Conference](https://img.shields.io/badge/EcuaHack-Ecuador_2018-g.svg) ![Conference](https://img.shields.io/badge/EkoParty-Argentina_2018-g.svg)

# Cómo funciona?
 El dispositivo funciona como un rubber ducky de hak5 con la diferencia que se pueden enviar los Scripts por medio de internet.
 
 ![Supported Python versions](https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/esquema.png)


# Hardware
Para este prototipo se uso Arduino Leonardo, que permite la inyección de palabras como si de un teclado se tratara, pero el 
proyecto  es compatible  con cualquier arduino  que tenga el micro ATmega32U4 como por  ejemplo  CJMCU o el  Arduino Micro.  

### Arduino Leonardo
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/20180906_162546.jpg" width="600" height="400" /> 



### CJMCU
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/20180906_162526.jpg" width="600" height="400" /> 

Ademas de un arduino necesitamos un módulo Wifi en este casi el  ESP8266 específicamente el  ESP-12 para este proyecto 
usamos un NodeMCU que facilita mucho las cosas a la hora de programar el ESP-12.

### NodeMCU
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/20180906_162517.jpg" width="600" height="400" /> 
 
 # Software
 Un programa escrito en python sirve como servidor socket, espera la conexión del dispistívo una vez conectado se puede modifcar, ver y enviar el script que se le enviará al dispositívo, el script que se enviara estara en la carpeta .../WBU/scritp.txt, el lenguaje que se usa es duckyscript  

## Instalación y Uso 
#### Hardware
- Conectar según el siguiente diagrama:
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/esquemaConexion.PNG" width="600" height="400" /> 
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/20180906_162647.jpg" width="600" height="400" /> 

- Subir los skechts al Arduino y al ESP(Nodemcu)

#### Software
```sh
# git clone https://github.com/miguelebf/WBU.git
# cd WBU
# python3 wbu.py
```

## To-do

 - Distribución del teclado (Keyboard Layouts) 
 - Comunicación por gsm/gprs
 - Desarrollar un dispositivo final

 ## Créditos

 - [WHID WiFi HID Injector](https://github.com/whid-injector/WHID) (funciones para convertir de Ducky Script a Arduino) 

Licencia
----

MIT
