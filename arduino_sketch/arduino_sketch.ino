#include <Servo.h> 
Servo myservo1; 
Servo myservo2; 
int pos = 0;
char rx_byte;

void setup() {
  Serial.begin(9600);
   myservo1.attach(5);
   myservo2.attach(19);
}

void loop() {
  static int v = 0;

  if ( Serial.available()) {
    char ch = Serial.read(); 
    switch(ch) {
      case 'q':
        myservo1.write(10);
         myservo2.write(10);
        v = 0;
        break;
      case 'w':
        myservo1.write(90);
        myservo2.write(90);
        v = 0;
        break; 
       case 'e':
        myservo1.write(170);
        myservo2.write(170);
        v = 0;
        break;
  }
}
}
