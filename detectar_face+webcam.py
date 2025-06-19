import cv2

# Carregar o classificador Haarcascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Abrir a webcam (0 é a webcam padrão)
camera = cv2.VideoCapture(0)

print("Pressione 'q' para sair.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    # Desenhar retângulos nas faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar resultado na tela
    cv2.imshow("Detecção Facial - Webcam", frame)

    # Sair com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
camera.release()
cv2.destroyAllWindows()
