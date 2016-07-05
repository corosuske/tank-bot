#include <VarSpeedServo.h>


VarSpeedServo myservo1; 
VarSpeedServo myservo2; 
int pos = 0;
char rx_byte;

void setup() {
  Serial.begin(9600);
   myservo1.attach(5, 0, 180);
   myservo2.attach(19, 0, 180);
}

void loop() {
  static int v = 0;d
  

  if ( Serial.available()) {
    char ch = Serial.read(); 
    switch(ch) {
      case 'd':
        myservo1.write(10);
         myservo2.write(10);
        v = 0;
        break;
      case 'e':
        myservo1.write(50);
        myservo2.write(50);
        v = 0;
        break;
      case 'w':
        myservo1.write(90);
        myservo2.write(90);
        v = 0;
        break; 
      case 'q':
        myservo1.write(130);
        myservo2.write(130);
        v = 0;
        break;
       case 'a':
        myservo1.write(170);
        myservo2.write(170);
        v = 20;
        break;
       case 'o':        
        myservo1.slowmove (0, 0);
       case 'p':        
        myservo1.slowmove (100, 180);
  }
}
}
