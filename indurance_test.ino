#include <Arduino.h>

const int relayPin = 13;
int cycleCounter = 0;

unsigned long startTime; // Variable to store the start time

void setup() {
  // Initialize 
  pinMode(relayPin, OUTPUT);

  // Start Serial Monitor
  Serial.begin(9600);
  Serial.println("Relay Control Started");

  // Record the start time
  startTime = millis();
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
    Serial.println(": Cycle Completed");
  } else {
    unsigned long endTime = millis(); // Record the end time
    Serial.println("450 cycles completed. Stopping.");
    Serial.print("Start Time: ");
    Serial.println(startTime);
    Serial.print("End Time: ");
    Serial.println(endTime);
    while (true) {
      // Keep the program running
    }
  }
}
