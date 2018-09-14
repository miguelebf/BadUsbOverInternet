//Librerias
#include <ESP8266WiFi.h>
//Variables
#define BAUD_RATE 9600
WiFiClient client;
int port=9999;
String host="192.168.0.3"; //Cambiar por ip del Servidor
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  //Serial 
  Serial.begin(BAUD_RATE);
  //Wifi 
  WiFi.begin("Anon", "mebfgeek");
  
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
  }
  //Conexion Socket
  while(true){
    if (client.connect(host,port)){
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
    Serial.println(script); 
  }
  delay(1000);
  if(Serial.available()){
    uint8_t respuesta = Serial.read();
    if(respuesta==0x1){
      client.print("1");
    }
    else{
      client.print("0");

      }
    }
  }
  //Reconexion Socket
  while(true){
    if (client.connect(host,port)){
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
