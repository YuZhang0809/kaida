# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:32:18 2021

@author: E
"""
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import numpy as np

mtcnn = MTCNN(image_size=160, margin=10)
model = InceptionResnetV1(pretrained='vggface2').eval()


image_path1 = "face_data/FaceCog/face.jpg"
image_path2 = "face_data/A/face4.jpg"


img1 = Image.open(image_path1)
img_cropped1 = mtcnn(img1) 
img_embedding1 = model(img_cropped1.unsqueeze(0))
 
img2 = Image.open(image_path2)
img_cropped2 = mtcnn(img2)
img_embedding2 = model(img_cropped2.unsqueeze(0))

# 類似度の関数
def cos_similarity(p1, p2): 
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

p1 = img_embedding1.squeeze().to('cpu').detach().numpy().copy()
p2 = img_embedding2.squeeze().to('cpu').detach().numpy().copy()
 
# 類似度を計算して顔認証
img1vs2 = cos_similarity(p1, p2)

print("類似度", img1vs2)