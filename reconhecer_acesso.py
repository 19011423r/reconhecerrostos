import cv2
import numpy as np
import os

# Carregar modelo treinado e labels
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("modelo_lbph.yml")

labels = np.load("labels.npy", allow_pickle=True).item()

# Inverter dicionário para pegar nome pelo label
labels_invertido = {v:k for k,v in labels.items()}

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

print("Pressione 'q' para sair.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor_
