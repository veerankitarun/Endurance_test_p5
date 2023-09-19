// Pin number to which the relay control input is connected
const int relayPin = 13; // Change this to your chosen GPIO pin

void setup() {
  // Initialize the relay control pin as an output
  pinMode(relayPin, OUTPUT);

  // Start communication with the Serial Monitor
  Serial.begin(9600);
  Serial.println("Relay Control Started");
}

void loop() {
  // Number of cycles per minute (15 cycles per minute)
  int cyclesPerMinute = 15;

  // Calculate the time for each cycle (in milliseconds)
  unsigned long cycleTime = 60000 / cyclesPerMinute;

  // Turn on the relay
  digitalWrite(relayPin, HIGH);
  Serial.println("Relay ON");
  delay(cycleTime / 2); // Keep it on for half of the cycle time

  // Turn off the relay
  digitalWrite(relayPin, LOW);
  Serial.println("Relay OFF");
  delay(cycleTime / 2); // Keep it off for half of the cycle time

  // Send "CycleCompleted" message to the serial port
  Serial.println("CycleCompleted");
}
