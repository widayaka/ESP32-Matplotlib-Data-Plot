#define OUTPUT_LED 2
#define INPUT_POTENTIOMETER 5
#define OUTPUT_VCC 6
#define OUTPUT_GND 4

int analogValue = 0;
char userInput;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(OUTPUT_LED, OUTPUT);
  pinMode(INPUT_POTENTIOMETER, INPUT);
  pinMode(OUTPUT_VCC, OUTPUT); digitalWrite(OUTPUT_VCC, HIGH);
  pinMode(OUTPUT_GND, OUTPUT); digitalWrite(OUTPUT_GND, LOW);
}

void loop() {
    if (Serial.available() > 0){
      userInput = Serial.read();
      if (userInput == 'g'){
        analogValue = analogRead(INPUT_POTENTIOMETER);
        Serial.println(analogValue);
      }
    }
    // analogValue = analogRead(INPUT_POTENTIOMETER);
    // Serial.println(analogValue);
}
