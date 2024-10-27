#include <Wire.h>

void setup() {
  Wire.begin();
  Serial.begin(9600);

  // Initialize camera (basic setup)
  initCamera();

  Serial.println("Camera initialized.");
}

void loop() {
  // Capture image or process data as needed
}

void initCamera() {
  Wire.beginTransmission(0x42); // OV7670 default I2C address
  Wire.write(0x12); // Reset register
  Wire.write(0x80); // Reset command
  Wire.endTransmission();

  delay(100);

  // Additional camera configuration here
}
