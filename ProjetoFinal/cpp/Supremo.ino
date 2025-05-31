#include <Servo.h>

Servo servo;
int pos = 90;  // Posição inicial do servo

void setup() {
    servo.attach(9);  // Conecta o servo ao pino D9
    Serial.begin(9600);
    randomSeed(analogRead(0));  // Inicializa números aleatórios com base no ruído do pino A0
}

void moveToPosition(int targetPos) {
    int stepSize = 2;  // Define o tamanho do passo para movimento suave
    if (targetPos > pos) {
        for (int i = pos; i <= targetPos; i += stepSize) {
            servo.write(i);
            delay(50);  // Pequena pausa para suavizar a transição
        }
    } else {
        for (int i = pos; i >= targetPos; i -= stepSize) {
            servo.write(i);
            delay(50);  // Pequena pausa para suavizar a transição
        }
    }
    pos = targetPos;  // Atualiza a posição atual
}

void loop() {
    // Gera uma posição aleatória dentro de um intervalo baseado na posição atual
    int randomDelta = random(-40, 40);  // Movimento aleatório dentro de uma variação limitada
    int randomTarget = constrain(pos + randomDelta, 0, 180);  // Garante que fique dentro dos limites

    moveToPosition(randomTarget);
    delay(random(1000, 3000));  // Espera um tempo aleatório antes de mudar de posição
}
