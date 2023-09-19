import processing.serial.*;

Serial arduino; // Serial communication with Arduino
int cycleCount = 0; // Variable to store cycle count
boolean cycling = false; // Variable to track if cycling is active

void setup() {
  size(200, 160);
  arduino = new Serial(this, "COM3", 9600); // Replace COMX with your Arduino's COM port
  textAlign(CENTER, CENTER);
}

void draw() {
  background(240);

  // Display cycle count
  fill(0);
  textSize(24);
  text(cycleCount, width/2, height/2 - 10);

  // Display cycling status
  textSize(16);
  if (cycling) {
    fill(0, 255, 0);
    text("", width/2, height/2 + 30);
  } else {
    fill(255, 0, 0);
    text("", width/2, height/2 + 30);
  }

  // Start button
  fill(0, 255, 0);
  rect(20, 110, 80, 30);
  fill(0);
  text("Start", 60, 125);

  // Stop button
  fill(255, 0, 0);
  rect(100, 110, 80, 30);
  fill(0);
  text("Stop", 140, 125);
}

void mousePressed() {
  if (mouseX >= 20 && mouseX <= 100 && mouseY >= 110 && mouseY <= 140) {
    // Send a command to start the cycle to Arduino
    arduino.write('1');
    cycling = true;
  } else if (mouseX >= 100 && mouseX <= 180 && mouseY >= 110 && mouseY <= 140) {
    // Send a command to stop the cycle to Arduino
    arduino.write('0');
    cycling = false;
  }
}

void serialEvent(Serial port) {
  String message = port.readStringUntil('\n');
  if (message != null) {
    message = trim(message);
    if (message.equals("CycleCompleted")) {
      // Increment the cycle count when the Arduino sends "CycleCompleted" message
      cycleCount++;
    }
  }
}
