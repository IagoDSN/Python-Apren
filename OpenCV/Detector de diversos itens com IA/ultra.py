import cv2
from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    results = model.predict(source=frame, conf=0.5, max_det=50, verbose=False)

    annotated_frame = results[0].plot()

    cv2.imshow("Detecção em Tempo Real", annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
