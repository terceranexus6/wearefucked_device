//may change, using rgb led
#define RLED 10
#define BLED 6
#define GLED 5

// Using http://slides.justen.eng.br/python-e-arduino as refference

void setup() {
    pinMode(BLED, OUTPUT);
    pinMode(GLED, OUTPUT);
    pinMode(RLED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == 'R') {
            digitalWrite(BLED, LOW);
            digitalWrite(GLED, LOW);
            digitalWrite(RLED, HIGH);
        }
        else if (serialListener == 'B') {
            digitalWrite(RLED, LOW);
            digitalWrite(GLED, LOW);
            digitalWrite(BLED, HIGH);
        }
        else if (serialListener == 'G') {
            digitalWrite(RLED, LOW);
            digitalWrite(BLED, LOW);
            digitalWrite(GLED, HIGH);
        }
        else{
            digitalWrite(RLED, LOW);
            digitalWrite(BLED, LOW);
            digitalWrite(GLED,LOW);
        }
      
    }
}
