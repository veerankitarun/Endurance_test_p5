#include <Arduino.h>

const int relayPin = 13; 
int cycleCounter = 0;   

void setup() {
  // Initialize 
  pinMode(relayPin, OUTPUT);

  // com Serial Monitor
  Serial.begin(9600);
  Serial.println("Relay Control Started");
}

void loop() {
  // Number of cycles per minute (15 cycles per minute)
  int cyclesPerMinute = 15;

  // Calculate the time for each cycle (in milliseconds)
  unsigned long cycleTime = 60000 / cyclesPerMinute;

  // Check if we haven't reached 450 cycles yet
  if (cycleCounter < 15) {
    // Increment the cycle counter
    cycleCounter++;

    // Turn on the relay
    digitalWrite(relayPin, HIGH);
    Serial.print("Cycle ");
    Serial.print(cycleCounter);
    Serial.println(": Relay ON");
    delay(cycleTime / 2);

  
    digitalWrite(relayPin, LOW);
    Serial.print("Cycle ");
    Serial.print(cycleCounter);
    Serial.println(": Relay OFF");
    delay(cycleTime / 2); 

  
    Serial.print("Cycle ");
    Serial.print(cycleCounter);
    Serial.println(": CycleCompleted");
  } else {
    
    Serial.println("450 cycles completed. Stopping.");
    while (true) {
      
    }
  }
}
