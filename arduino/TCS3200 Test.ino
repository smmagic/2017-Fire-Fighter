/*
 * Brandon Waller 
 * Code for TCS 3200 Color Sensor
 * Output R,G,B to serial
 * can be used ot return values to python
 */

#define s0 9
#define s1 10
#define s2 11
#define s3 12
#define sensorOut 13 
//LED pin not needed but can be used by connecting 5v -> resistor -> LED Pin

int red = 0, blue = 0, green = 0;
void setup() {
  pinMode(s0, OUTPUT);  
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(sensorOut, INPUT);

  digitalWrite(s0, HIGH);
  digitalWrite(s1, LOW);

  Serial.begin(9600);
}

void loop() {

  //RED
  digitalWrite(s2, HIGH);
  digitalWrite(s3, LOW);

  red = pulseIn(sensorOut, LOW);
  delay(100);

  //GREEN
  digitalWrite(s2, HIGH);
  digitalWrite(s3,HIGH);

  green = pulseIn(sensorOut, LOW);;
  delay(100);

  //BLUE
  digitalWrite(s2, LOW);
  digitalWrite(s3, HIGH);

  blue = pulseIn(sensorOut, LOW);

  String output = String(red) + "," + String(green) + "," + String(blue);
  Serial.println(output);

  delay(2000);
}
