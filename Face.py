# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:13:24 2021

@author: E
"""

import cv2

face_cascade_path = "./face_data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 分類器で顔のx座標,y座標,幅,高さを取得
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # 各顔について
    for x, y, w, h in faces:

        # 顔の外接短形を描画
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = img[y : y + h, x : x + w]
        face_gray = gray[y : y + h, x : x + w]
        
    # ウィンドウに結果を表示
    cv2.imshow("video image", img)

    # 終了オプション
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

# 終了処理
cv2.destroyAllWindows()
cap.release()