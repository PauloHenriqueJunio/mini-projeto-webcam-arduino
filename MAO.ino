#define LED_VERDE 10

void setup() {
  pinMode(LED_VERDE, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == '1') {
      digitalWrite(LED_VERDE, HIGH);
    } 
    else if (comando == '0') {
      digitalWrite(LED_VERDE, LOW);
    }
  }
}