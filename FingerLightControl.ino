int ledPin = 13; // Pin connected to the LED

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(ledPin, HIGH); // Turn the LED on
    } else if (command == '0') {
      digitalWrite(ledPin, LOW); // Turn the LED off
    }
  }
}
