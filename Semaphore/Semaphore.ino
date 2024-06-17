short colors[] = {2,4,5};
short LedPin = 0;
int colorSize = sizeof(colors) / sizeof(colors[0]);
int semaphoreState = 0;

void setup() {
  Serial.begin(9600);
  for( short i = 0; i < colorSize; i++ ){
    pinMode(colors[i], OUTPUT);
  }
  LedPin = colors[semaphoreState];
  delay(1000);
  Serial.print("========================\n");
  Serial.print("        Semaphore       \n");
  Serial.print("========================\n");  
}

void loop() {
  digitalWrite(LedPin, HIGH);
  delay(1500);
  digitalWrite(LedPin, LOW);
  semaphoreState++;
  if( semaphoreState == colorSize ){
    semaphoreState = 0;
  }
  LedPin = colors[semaphoreState];
  delay(500);
}
