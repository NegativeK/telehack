#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"
// Interduino is the physical manifestation of cigtee - an arduino sketch designed to take serial commands to make stuff happen IRL


void setup()
{
for(int i=3; i<9; i++) {
	pinMode(i, OUTPUT);
	}
Serial.begin(9600);

}

int pinState[6];

void loop()
{
if(Serial.available() > 2) {
	int pin = Serial.read();
	pinState[pin] = Serial.read();
	int duration = Serial.read();
	}
}
