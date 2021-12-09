# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:13:24 2021

@author: E
"""

import cv2
import time

face_cascade_path = "./face_data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)

cap = cv2.VideoCapture(0)

start_time = 0
end_time = 0
count_face = 1
count_background = 1


# スクショしたかどうかを保存する変数 (まだ撮っていないのでFalse)
screenshot = False
# スクショを保存する変数
photo = None

# 実行
while True:
    # Webカメラのフレーム取得
    ret, img = cap.read()
    # キーボードの入力の受付
    k = cv2.waitKey(1)
    cv2.imshow("video image", img)
    
    # 終了
    if k == ord("q"):
        break
    # 背景の写真を保存
    elif k == ord("s") and count_background < 20:
        cv2.imwrite('face_data/background/background' + str(count_background) + '.jpg', img)
        count_background += 1
        time.sleep(0.1)
    
    # 顔の写真を保存
    elif k == ord("c"):
    # グレースケールに変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 分類器で顔のx座標,y座標,幅,高さを取得
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # 各顔について
        for x, y, w, h in faces:
        
            # 顔の外接短形を描画
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = img[y : y + h, x : x + w]  
            cv2.imshow("face image", face)
            if count_face < 20:
                count_face += 1
                print('face_data/sho' + str(count_face) + '.jpg')
                cv2.imwrite('face_data/sho/face' + str(count_face) + '.jpg',face)  
            face_gray = gray[y : y + h, x : x + w]
        
# 終了処理
cv2.destroyAllWindows()
cap.release()