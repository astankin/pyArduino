int cnt = 1;
int DL = 100;
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.print(cnt);
Serial.println(" Mississippi");
cnt = cnt + 1;
delay(DL);
}