
# Sistema de Reconhecimento Facial para Controle de Acesso Escolar

## Descrição

Este projeto implementa um sistema de reconhecimento facial em Python usando OpenCV para permitir o acesso apenas a pessoas cadastradas, visando aumentar a segurança em escolas.

## Estrutura do Projeto

- `capturar_cadastro.py`: Captura e salva imagens dos rostos para cadastro.
- `detectar_face_webcam.py`: Detecta rostos em tempo real pela webcam.
- `treinar_modelo.py`: Treina o modelo LBPH com as imagens capturadas.
- `reconhecer_acesso.py`: Reconhece rostos em tempo real e libera ou nega acesso.

## Como usar

1. Crie e ative o ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
