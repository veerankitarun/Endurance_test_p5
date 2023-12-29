#include <Arduino.h>
const int relayPin = 13;
int cycleCounter = 0;
int totalCycles = 0; // Variable to store the total number of cycles
unsigned long startTime; // Variable to store the start time
void setup() {
  // Initialize
  pinMode(relayPin, OUTPUT);
  // Start Serial Monitor
  Serial.begin(9600);
  Serial.println("Indurance Test Started");
  // Get the total number of cycles from the user
  Serial.print("Enter the number of cycles to run:\n ");
  while (!Serial.available()) {
    // Wait for user input
  }
  totalCycles = Serial.parseInt(); // Read user input as an integer
  // Record the start time
  startTime = millis();
}
void loop() {
  // Number of cycles per minute (15 cycles per minute)
  int cyclesPerMinute = 15;
  // Calculate the time for each cycle (in milliseconds)
  unsigned long cycleTime = 60000 / cyclesPerMinute;
  // Check if we haven't reached the total number of cycles yet
  if (cycleCounter < totalCycles) {
    // Increment the cycle counter
    cycleCounter++;
    // Turn on the relay
    digitalWrite(relayPin, HIGH);
    Serial.print("Cycle ");
    Serial.print(cycleCounter);
    Serial.println(": Relay ON");
    delay(cycleTime / 2);
    digitalWrite(relayPin, LOW);
    Serial.print(" Cycle ");
    Serial.print(cycleCounter);
    Serial.println(": Relay OFF");
    delay(cycleTime / 2);
    // Serial.print("Cycle ");
    // Serial.print(cycleCounter);
    // Serial.println(": Cycle Completed");
  } else {
    unsigned long endTime = millis(); // Record the end time
    Serial.print(cycleCounter);
    Serial.println(" cycles completed and Stoped. \n");
    // Serial.print("Start Time: ");
    // Serial.println(startTime);
    // Serial.print("End Time: ");
    // Serial.println(endTime);
    while (true) {
      // Keep the program running
    }
  }
}