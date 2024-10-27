#include <Wire.h>

// OV7670 Registers (minimal set for basic setup)
#define REG_COM7 0x12
#define REG_CLKRC 0x11

// Pin Definitions (adjusted to match the new pin configuration)
#define XCLK_PIN 13     // PWM capable pin for external clock
#define PCLK_PIN 12     // Pixel Clock (OV7670)
#define VSYNC_PIN 11    // Vertical Sync (OV7670)
#define HREF_PIN 10     // Horizontal Reference (OV7670)

// Data pins D0-D7 connected to digital pins 2-9
#define D0_PIN 2
#define D1_PIN 3
#define D2_PIN 4
#define D3_PIN 5
#define D4_PIN 6
#define D5_PIN 7
#define D6_PIN 8
#define D7_PIN 9

void setup() {
  // Setup serial communication
  Serial.begin(115200);
  
  // Initialize I2C for camera configuration
  Wire.begin();
  
  // Set the XCLK pin to generate clock
  pinMode(XCLK_PIN, OUTPUT);
  analogWrite(XCLK_PIN, 128);  // Generate 8MHz clock signal using PWM

  // Set pins for reading camera signals
  pinMode(PCLK_PIN, INPUT);
  pinMode(VSYNC_PIN, INPUT);
  pinMode(HREF_PIN, INPUT);

  // Set data pins D0-D7 as inputs
  for (int i = D0_PIN; i <= D7_PIN; i++) {
    pinMode(i, INPUT);
  }

  // Initialize the camera
  cameraInit();
}

void loop() {
  if (digitalRead(VSYNC_PIN) == LOW) {
    // Start reading a frame when VSYNC goes low
    Serial.println("Capturing frame...");
    
    for (int row = 0; row < 144; row++) {   // Adjust resolution if necessary
      for (int col = 0; col < 176; col++) { // Adjust resolution if necessary
        if (digitalRead(HREF_PIN) == HIGH) {
          // Wait for pixel clock pulse to read pixel data
          if (digitalRead(PCLK_PIN) == HIGH) {
            uint8_t pixelData = readPixel();  // Read pixel data from D0-D7
            Serial.write(pixelData);  // Send pixel data over serial for debugging or further processing
          }
        }
      }
    }
    Serial.println("Frame captured");
  }
}

// Function to initialize the camera (basic settings)
void cameraInit() {
  // Camera basic configuration for QQVGA (160x120) or similar
  writeCameraRegister(REG_COM7, 0x04);  // Set QQVGA resolution
  writeCameraRegister(REG_CLKRC, 0x80);  // Set internal clock pre-scalar
  
  // Additional setup registers can go here based on your requirements
}

// Function to write a value to the OV7670 camera register via I2C
void writeCameraRegister(uint8_t reg, uint8_t value) {
  Wire.beginTransmission(0x42);  // Camera I2C address (OV7670 default)
  Wire.write(reg);
  Wire.write(value);
  Wire.endTransmission();
}

// Function to read a byte of pixel data from D0-D7
uint8_t readPixel() {
  uint8_t pixel = 0;
  
  // Read the bits from D0 to D7 and combine them into a single byte
  for (int i = 0; i < 8; i++) {
    pixel |= (digitalRead(D0_PIN + i) << i);  // Read digital pins 2-9 (D0-D7)
  }
  
  return pixel;
}
