
int latchPin = 5;
int clockPin = 6;
int dataPin = 4;
int latchPin2 = 8;
int dataPin2 = 7;

int decoder_pin1 = 10;
int decoder_pin2 = 11;
int decoder_pin3 = 12;
int decoder_pin4 = 13;

const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

byte leds = 0;
byte leds2 = 0;
char one = 'a';
char two = 'd';
char count = one;
int first = 1;

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" 
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(latchPin2, OUTPUT);
  pinMode(dataPin2, OUTPUT);
  pinMode(decoder_pin1, OUTPUT);
  pinMode(decoder_pin2, OUTPUT);
  pinMode(decoder_pin3, OUTPUT);
  pinMode(decoder_pin4, OUTPUT);
}


void loop() {
  char inByte = ' ';

    // read the state of the pushbutton value:
    buttonState = digitalRead(buttonPin);
    
    // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
    if (buttonState == HIGH) {
      // turn LED on:
      Serial.println(1, BIN); // send the data back in a new line so that it is not all one long line

      digitalWrite(ledPin, HIGH);
    } else {
      // turn LED off:
      digitalWrite(ledPin, LOW);
    }
  
  if(Serial.available()){ // only send data back if data has been sent
    char inByte = Serial.read(); // read the incoming data
    Serial.println(inByte, BIN); // send the data back in a new line so that it is not all one long line

   if (first == 1)
   {
        leds = inByte;
        first = 0;
   }
   else
   {
   
       char data = inByte;
       first = 1;

       if ((data & 1) == 1)
       {
        digitalWrite(decoder_pin1, HIGH);
       }
       else
       {
          digitalWrite(decoder_pin1, LOW);
      
       }
       
       if ((data & 2) == 2)
       {
        digitalWrite(decoder_pin2, HIGH);
       }
       else
       {
        digitalWrite(decoder_pin2, LOW);
       }
       
       if ((data & 4 ) == 4)
       {
        digitalWrite(decoder_pin3, HIGH);
       }
       else
       {
         digitalWrite(decoder_pin3, LOW);
       }
       
       if ((data & 8 ) == 8)
       {
        digitalWrite(decoder_pin4, HIGH);
       }
       else
       {
         digitalWrite(decoder_pin4, LOW);
       }
       
       
      updateShiftRegister1();
      //delay(200);
    
    
   }
  }
}



void updateShiftRegister1()
{
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, leds);
  digitalWrite(latchPin, HIGH);
}

void updateShiftRegister2()
{
  digitalWrite(latchPin2, LOW);
  shiftOut(dataPin2, clockPin, LSBFIRST, leds2);
  digitalWrite(latchPin2, HIGH);
}
