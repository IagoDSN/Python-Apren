import cv2
from ultralytics import YOLO
import torch
import pyttsx3
import time

model = YOLO("yolov8n.pt")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("Pressione 'q' para sair.")

def speak(text):
    """Converter texto em fala usando pyttsx3."""
    engine.say(text)
    engine.runAndWait()

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
        print(f"Objetcs detecteds: {objects_to_speak}")
        
        speak(f"I detected: {objects_to_speak}")
    else:
        print("Any object dected.")
        speak("Any object dected.")

    annotated_frame = results[0].plot()
    cv2.imshow("Detecção em Tempo Real", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(5)

cap.release()
cv2.destroyAllWindows()