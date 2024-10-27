#include <Wire.h>
#include <OV7670.h>

OV7670 camera;

void setup() {
    Serial.begin(9600);
    camera.begin();
    camera.setResolution(OV7670_640x480);
}

void loop() {
    camera.captureFrame();
    // Process the image data
    // For example, send it over Serial or save to an SD card
}
