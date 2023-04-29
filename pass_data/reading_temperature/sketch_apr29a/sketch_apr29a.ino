#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

float tempF;
float tempC;
float humidity;

int setTime = 500;
int dt = 1000;

DHT TH(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
TH.begin();
delay(setTime);
}

void loop() {
  // put your main code here, to run repeatedly:
tempC=TH.readTemperature(true);
tempF=TH.readTemperature();
humidity=TH.readHumidity();

Serial.print(tempF);
Serial.print(",");
Serial.print(tempC);
Serial.print(",");
Serial.println(humidity);

delay(dt); 
}
