int potPin = A0;
int potVal;
int DL = 100;
void setup() {
  // put your setup code here, to run once:
pinMode(potPin,INPUT);
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
potVal = analogRead(potPin);
Serial.println(potVal);
delay(DL);
}

