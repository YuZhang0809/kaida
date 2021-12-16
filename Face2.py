# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:13:24 2021

@author: E
"""

import cv2
import time
from PIL import Image
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1

#  open cv2
face_cascade_path = "./face_data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)
#  mtcnn
mtcnn = MTCNN(image_size=160, margin=10)
model = InceptionResnetV1(pretrained='vggface2').eval()

cap = cv2.VideoCapture(0)

start_time = 0
end_time = 0
count_face = 1
count_background = 1


# スクショしたかどうかを保存する変数 (まだ撮っていないのでFalse)
screenshot = False
# スクショを保存する変数
photo = None
image_path_A = "face_data/A/face4.jpg"

def cos_similarity(p1, p2): 
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

# 実行
while True:
    # Webカメラのフレーム取得
    ret, img = cap.read()
    # キーボードの入力の受付
    k = cv2.waitKey(10)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(img1)
    
    # 終了  
    if k == ord("q"):
        break
    
    # 顔認識
    elif k == ord("m"):
        faces = mtcnn(pil_im)
        boxes, _ = mtcnn.detect(pil_im)
        if boxes is None:
            time.sleep(0.2)
            continue
        else:
            try:
                for i,box in enumerate(boxes):
                    new_box = box.tolist()
                    x1, y1, width, height = int(new_box[0]), int(new_box[1]), int(new_box[2]), int(new_box[3])
                    cv2.rectangle(img, (x1, y1 + height),(x1 + int(width/1.25), y1), (255, 0, 0), 5)
                    new_face = img[y1 : y1 + height, x1 : x1 + width]
                    new_PILface = cv2.cvtColor(new_face, cv2.COLOR_BGR2RGB)    
                    img_cropped1 = mtcnn(new_PILface) 
                    img_embedding1 = model(img_cropped1.unsqueeze(0))
                    img_A = Image.open(image_path_A)
                    img_cropped2 = mtcnn(img_A)
                    img_embedding2 = model(img_cropped2.unsqueeze(0))  
                    p1 = img_embedding1.squeeze().to('cpu').detach().numpy().copy()
                    p2 = img_embedding2.squeeze().to('cpu').detach().numpy().copy()
                    img1vs2 = cos_similarity(p1, p2)
                    if img1vs2 >= 0.7:
                        cv2.putText(img,
                                    text='This is A',
                                    org=(int(x1+width/2), int(y1+height/2)),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1.0,
                                    color=(0, 255, 0),
                                    thickness=2,
                                    lineType=cv2.LINE_4)
                    else:
                        cv2.putText(img,
                                    text='This is ???',
                                    org=(int(x1+width/2), int(y1+height/2)),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1.0,
                                    color=(0, 255, 0),
                                    thickness=2,
                                    lineType=cv2.LINE_4)
                        
            except Exception as e:
                print(e)
                
                    
            
    # 背景の写真を保存
    elif k == ord("b") and count_background < 20:
        cv2.imwrite('face_data/background/background' + str(count_background) + '.jpg', img)
        count_background += 1
        time.sleep(0.1)
    
    # 顔の写真を保存
    elif k == ord("f"):
    # グレースケールに変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 分類器で顔のx座標,y座標,幅,高さを取得
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # 各顔について
        for x, y, w, h in faces:
        
            # 顔の外接短形を描画、平均値
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = img[y : y + h, x : x + w]  
            cv2.imshow("face image", face)
            if count_face < 20:
                count_face += 1
                print('face_data/sho' + str(count_face) + '.jpg')
                cv2.imwrite('face_data/A/face' + str(count_face) + '.jpg',face)  
            face_gray = gray[y : y + h, x : x + w]
            
    cv2.imshow("video image", img)
        
# 終了処理
cv2.destroyAllWindows()
cap.release()