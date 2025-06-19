import cv2
import os
import numpy as np

# Pasta com os dados (rostos) já capturados
dataset_path = "dataset"

# Função para carregar imagens e labels
def carregar_imagens_e_labels(path):
    imagens = []
    labels = []
    label_ids = {}
    id_atual = 0

    for nome_pessoa in os.listdir(path):
        pasta_pessoa = os.path.join(path, nome_pessoa)
        if not os.path.isdir(pasta_pessoa):
            continue
        if nome_pessoa not in label_ids:
            label_ids[nome_pessoa] = id_atual
            id_atual += 1
        label_id = label_ids[nome_pessoa]

        for arquivo in os.listdir(pasta_pessoa):
            if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
                imagem_path = os.path.join(pasta_pessoa, arquivo)
                imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
                if imagem is None:
                    continue
                imagens.append(imagem)
                labels.append(label_id)

    return imagens, labels, label_ids

print("Carregando imagens e labels...")
imagens, labels, label_ids = carregar_imagens_e_labels(dataset_path)

print(f"Imagens carregadas: {len(imagens)}")
print(f"Labels: {label_ids}")

# Criar o reconhecedor LBPH
reconhecedor = cv2.face.LBPHFaceRecognizer_create()

print("Treinando o modelo...")
reconhecedor.train(imagens, np.array(labels))

# Salvar o modelo e as labels
reconhecedor.save("modelo_lbph.yml")
with open("labels.npy", "wb") as f:
    np.save(f, label_ids)

print("Treinamento concluído e modelo salvo como 'modelo_lbph.yml'")
