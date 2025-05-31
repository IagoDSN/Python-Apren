#include <Servo.h>

Servo servo;
int pos = 90;  // Posição inicial do servo

void setup() {
    servo.attach(9);  // Conecta o servo ao pino D9
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        int servo_angle = Serial.parseInt();  // Lê o ângulo do Python
        pos = constrain(servo_angle, 0, 180);  // Garante que o ângulo está entre 0° e 180°
        servo.write(pos);  // Move o servo
        delay(20);  // Suaviza o movimento
    }
}
