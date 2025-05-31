import cv2
from ultralytics import YOLO
import torch
import pyttsx3
import time
import threading
import serial

# Inicializa comunicação serial com o Arduino
arduino = serial.Serial('COM3', 9600, timeout=1) 

model = YOLO("yolov8n.pt")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("Pressione 'q' para sair.")

last_spoken_time = 0
speak_interval = 2

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    results = model.predict(source=frame, conf=0.5, max_det=50, verbose=False)
    detections = results[0].boxes.data
    detected_objects = []

    if len(detections) > 0:
        for box in detections:
            class_id = int(box[5])
            class_name = model.names[class_id]
            detected_objects.append(class_name)

        objects_to_speak = ", ".join(set(detected_objects))
        print(f"Objetos detectados: {objects_to_speak}")

        current_time = time.time()
        if current_time - last_spoken_time >= speak_interval:
            speak(f"I detected: {objects_to_speak}")
            last_spoken_time = current_time

        # Envia a quantidade de objetos para o Arduino
        object_count = len(set(detected_objects))
        arduino.write(f"{object_count}\n".encode())  

    else:
        print("Nenhum objeto detectado.")
        current_time = time.time()
        if current_time - last_spoken_time >= speak_interval:
            speak("No objects detected.")
            last_spoken_time = current_time

    annotated_frame = results[0].plot()
    cv2.imshow("Detecção em Tempo Real", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

'''
#include <Servo.h>

Servo servo;
int pos = 90;  // Posição inicial do servo

void setup() {
    servo.attach(9);  // Conecta o servo ao pino D9
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        int object_count = Serial.parseInt();  // Lê dados via Serial
        if (object_count > 0) {
            pos = constrain(object_count * 10, 0, 180);  // Ajusta posição entre 0° e 180°
            servo.write(pos);
        }
        delay(500);  // Pequena pausa para evitar movimentos bruscos
    }
}
'''