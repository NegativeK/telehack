// Interduino is the physical manifestation of cigtee - an arduino sketch designed to take serial commands to make stuff happen IRL


void setup()
{
	Serial.begin(9600);
	pinMode(4, OUTPUT);

}

int pinState[6];

void loop()
{
	if(Serial.available()){
		int ledState = Serial.read();
		if(ledState == 65){
			digitalWrite(4, HIGH);
			delay(10000);
			digitalWrite(4, LOW);
		}
//		if(ledState == 90){ 
//			digitalWrite(4, LOW);
//		}
	}
}

