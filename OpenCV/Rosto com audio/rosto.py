import cv2
import subprocess
import os

# Inicializar captura de vídeo
cap = cv2.VideoCapture(0)

# Carregar o classificador de detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Configurar a janela em tela cheia
cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Frame', cv2.WINDOW_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Variável para controlar se o áudio foi reproduzido
audio_played = False

# Verificação do caminho absoluto para o arquivo de áudio
audio_filename = 'msg.mp3'
audio_directory = r'C:\Users\iagod\piton'  # Atualize este caminho para o diretório correto
audio_path = os.path.join(audio_directory, audio_filename)

if not os.path.exists(audio_path):
    print(f"Arquivo de áudio não encontrado: {audio_path}")
else:
    print(f"Arquivo de áudio encontrado: {audio_path}")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Melhorar contraste e suavizar a imagem
    gray = cv2.equalizeHist(gray)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Desenhar círculos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        radius = max(w, h) // 2
        cv2.circle(frame, center, radius, (255, 0, 0), 2)
        cv2.putText(frame, 'Rosto', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Reproduzir áudio se um rosto for detectado e se o áudio ainda não foi reproduzido
        if not audio_played and os.path.exists(audio_path):
            subprocess.Popen(['start', 'wmplayer', audio_path], shell=True)
            audio_played = True
    
    # Mostrar o frame com as detecções
    cv2.imshow('Frame', frame)
    
    # Sair do loop ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
