import cv2
from ultralytics import YOLO
import torch
import serial
import time
import threading

# Inicializa a comunicação serial
arduino = serial.Serial('COM3', 9600, timeout=1)  

model = YOLO("yolov8n.pt")

# Inicializa a câmera
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

searching = True
servo_angle = 90
patrol_direction = -2

def send_angle(angle):
    """ Envia o ângulo para o Arduino """
    global servo_angle
    arduino.write(f"{angle}\n".encode())
    servo_angle = angle
    time.sleep(0.05)

def patrol():
    global searching, servo_angle, patrol_direction
    while searching:
        servo_angle += patrol_direction
        if servo_angle <= 0 or servo_angle >= 180: 
            patrol_direction *= -1  
        send_angle(servo_angle)
        time.sleep(0.05)

# Inicia a patrulha em uma thread separada
patrol_thread = threading.Thread(target=patrol)
patrol_thread.daemon = True
patrol_thread.start()

print("Pressione 'q' para sair.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    results = model.predict(source=frame, conf=0.5, max_det=50, verbose=False)
    detections = results[0].boxes.data

    persons = [box for box in detections if model.names[int(box[5])] == "person"]

    if persons:
        searching = False  
        target = min(persons, key=lambda b: abs((b[0] + b[2]) / 2 - 320))  
        x_center = (target[0] + target[2]) / 2 
        
        normalized_x = 1 - (x_center / 640)  
        servo_angle = int(normalized_x * 180)  

        send_angle(servo_angle)  
        print(f"Pessoa detectada! Servo ajustado para {servo_angle}°")

    else:
        if not searching: 
            searching = True
            patrol_thread = threading.Thread(target=patrol) 
            patrol_thread.daemon = True
            patrol_thread.start()

    annotated_frame = results[0].plot()
    cv2.imshow("Detecção em Tempo Real", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
