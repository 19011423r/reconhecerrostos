import cv2
import os

# Nome do usuário para cadastro (pode modificar antes de rodar)
nome_usuario = input("Digite o nome da pessoa para cadastro: ")

# Diretório para salvar as imagens
diretorio = f"dataset/{nome_usuario}"
os.makedirs(diretorio, exist_ok=True)

# Carrega o classificador Haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

print("Pressione 'c' para capturar o rosto, 'q' para sair.")

contador = 0
max_imagens = 20  # Número máximo de imagens por pessoa

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.de_
