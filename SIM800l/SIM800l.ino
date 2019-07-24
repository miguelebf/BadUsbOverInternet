//Librerias
#include <gprs.h>

//Variables
#define BAUD_RATE 9600
GPRS client;

int port=9999;
String host="192.168.0.3"; //Cambiar por ip del Servidor
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  //Serial 
  Serial.begin(BAUD_RATE);
  //GPRS
  gprs.preInit();
  while(0 != gprs.init()) {
     delay(1000);
     Serial.println("init error");
  }  
  while(!gprs.join("internet.movistar.com.ec")) {//APN
      Serial.println("Error joining GPRS network");
      delay(2000);
  }
  
  //Conexion Socket
  while(true){
    if (client.connectTCP(host,port)){
      break;
    }
    else{
      continue;
    }
  }
}
void loop() { 
 while(client.connected()){
  if (client.available()){
    parpadearNodeMCU();
    String script = client.readStringUntil('\r');
      if(debug){
      Serial.println(script);
      }
      if(script.length() > 0){  
        script.replace("\r","\n");  
        while(script.length() > 0){  
        int latest_return = script.indexOf("\n");
        if(latest_return == -1){
        proscesarLinea(script);
        script = "";
        }
        else{
        if(debug){
        Serial.println("run: '"+script.substring(0, latest_return)+"'");
        }
        proscesarLinea(script.substring(0, latest_return));
        script = script.substring(latest_return + 1);  
      }
     }
      script = "";
      ExternSerial.write(0x1);  
    } 
  }
  delay(1000);
  }
  //Reconexion Socket
  while(true){
    if (client.connectTCP(host,port)){
      break;
    }
    else{
      continue;
    }
  }
}
 
void parpadearNodeMCU(){
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);               
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
 }

 void proscesarLinea(String _line)
{
  int firstSpace = _line.indexOf(" ");
  if(firstSpace == -1) presionarTecla(_line);
  else if(_line.substring(0,firstSpace) == "STRING"){
    for(int i=firstSpace+1;i<_line.length();i++) Keyboard.write(_line[i]);
  }
  else if(_line.substring(0,firstSpace) == "DELAY"){
    int delaytime = _line.substring(firstSpace + 1).toInt();
    delay(delaytime);
  }
  else if(_line.substring(0,firstSpace) == "DEFAULTDELAY") defaultDelay = _line.substring(firstSpace + 1).toInt();
  else if(_line.substring(0,firstSpace) == "REM"){} //nothing :/
  else if(_line.substring(0,firstSpace) == "REPLAY") {
    int replaynum = _line.substring(firstSpace + 1).toInt();
    while(replaynum)
    {
      proscesarLinea(last);
      --replaynum;
    }
  } else{
      String remain = _line;

      while(remain.length() > 0){
        int latest_space = remain.indexOf(" ");
        if (latest_space == -1){
          presionarTecla(remain);
          remain = "";
        }
        else{
          presionarTecla(remain.substring(0, latest_space));
          remain = remain.substring(latest_space + 1);
        }
        delay(5);
      }
  }

  Keyboard.releaseAll();
  delay(defaultDelay);
}

void presionarTecla(String b){
  if(b.length() == 1) Keyboard.press(char(b[0]));
  else if (b.equals("ENTER")) Keyboard.press(KEY_RETURN);
  else if (b.equals("CTRL")) Keyboard.press(KEY_LEFT_CTRL);
  else if (b.equals("SHIFT")) Keyboard.press(KEY_LEFT_SHIFT);
  else if (b.equals("ALT")) Keyboard.press(KEY_LEFT_ALT);
  else if (b.equals("GUI")) Keyboard.press(KEY_LEFT_GUI);
  else if (b.equals("UP") || b.equals("UPARROW")) Keyboard.press(KEY_UP_ARROW);
  else if (b.equals("DOWN") || b.equals("DOWNARROW")) Keyboard.press(KEY_DOWN_ARROW);
  else if (b.equals("LEFT") || b.equals("LEFTARROW")) Keyboard.press(KEY_LEFT_ARROW);
  else if (b.equals("RIGHT") || b.equals("RIGHTARROW")) Keyboard.press(KEY_RIGHT_ARROW);
  else if (b.equals("DELETE")) Keyboard.press(KEY_DELETE);
  else if (b.equals("PAGEUP")) Keyboard.press(KEY_PAGE_UP);
  else if (b.equals("PAGEDOWN")) Keyboard.press(KEY_PAGE_DOWN);
  else if (b.equals("HOME")) Keyboard.press(KEY_HOME);
  else if (b.equals("ESC")) Keyboard.press(KEY_ESC);
  else if (b.equals("BACKSPACE")) Keyboard.press(KEY_BACKSPACE);
  else if (b.equals("INSERT")) Keyboard.press(KEY_INSERT);
  else if (b.equals("TAB")) Keyboard.press(KEY_TAB);
  else if (b.equals("END")) Keyboard.press(KEY_END);
  else if (b.equals("CAPSLOCK")) Keyboard.press(KEY_CAPS_LOCK);
  else if (b.equals("F1")) Keyboard.press(KEY_F1);
  else if (b.equals("F2")) Keyboard.press(KEY_F2);
  else if (b.equals("F3")) Keyboard.press(KEY_F3);
  else if (b.equals("F4")) Keyboard.press(KEY_F4);
  else if (b.equals("F5")) Keyboard.press(KEY_F5);
  else if (b.equals("F6")) Keyboard.press(KEY_F6);
  else if (b.equals("F7")) Keyboard.press(KEY_F7);
  else if (b.equals("F8")) Keyboard.press(KEY_F8);
  else if (b.equals("F9")) Keyboard.press(KEY_F9);
  else if (b.equals("F10")) Keyboard.press(KEY_F10);
  else if (b.equals("F11")) Keyboard.press(KEY_F11);
  else if (b.equals("F12")) Keyboard.press(KEY_F12);
  else if (b.equals("SPACE")) Keyboard.press(' ');
}
