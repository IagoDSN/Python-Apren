import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Configure o dispositivo de vídeo virtual do DroidCam (substitua por 0 ou outro índice, se necessário)
camera_index = 0
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

print("Pressione 'q' para sair.")

while True:
    # Capturar frames da câmera USB
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break
    results = model.predict(source=frame, conf=0.5, max_det=50, verbose=False)

    annotated_frame = results[0].plot()
    cv2.imshow("Detecção com Câmera USB", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

