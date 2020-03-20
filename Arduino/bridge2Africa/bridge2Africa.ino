
int latchPin = 5;
int clockPin = 6;
int dataPin = 4;
int latchPin2 = 8;
int dataPin2 = 7;

byte leds = 0;
byte leds2 = 0;
char one = 'a';
char two = 'd';
char count = one;
int first = 1;



void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" 
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(latchPin2, OUTPUT);
  pinMode(dataPin2, OUTPUT);
}



void loop() {
  
  char inByte = ' ';
  if(Serial.available()){ // only send data back if data has been sent
    char inByte = Serial.read(); // read the incoming data
    Serial.println(inByte); // send the data back in a new line so that it is not all one long line

   if (first == 1)
   {
    leds = inByte;
    first = 0;
   }
   else
   {
   leds2 = inByte;
   first = 1;
   
   //leds = 6; //sets the 1st IC segment to have a byte value of 6 so this value is the input that should be received
    updateShiftRegister1();
    delay(200);
    //leds2 = 9;
    updateShiftRegister2();
    
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
