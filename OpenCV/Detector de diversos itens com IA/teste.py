import torch
import torchvision
import cv2
import numpy as np

# Carregar modelo pré-treinado SSDlite com MobileNetV3
model = torchvision.models.detection.ssdlite320_mobilenet_v3_large(pretrained=True)
model.eval()

COCO_CLASSES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag',
    'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
    'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
    'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
    'toilet', 'TV', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Abrir webcam padrão
cap = cv2.VideoCapture(1)

# Configurar janela em tela cheia
cv2.namedWindow('Detecção de Objetos', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Detecção de Objetos', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Não foi possível capturar o frame da câmera")
        break

    # Preprocessar frame: BGR para RGB e normalizar
    input_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) / 255.0
    input_tensor = torch.from_numpy(input_frame).permute(2, 0, 1).unsqueeze(0).float()

    with torch.no_grad():
        detections = model(input_tensor)[0]

    for i in range(len(detections['boxes'])):
        score = detections['scores'][i].item()
        if score > 0.7:
            box = detections['boxes'][i].cpu().numpy().astype(int)
            class_id = detections['labels'][i].item()
            x1, y1, x2, y2 = box

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{COCO_CLASSES[class_id]}: {score:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Detecção de Objetos', frame)

    # Sai do loop se apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
