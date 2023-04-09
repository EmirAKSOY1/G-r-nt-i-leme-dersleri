#mavi renk takip

import numpy as np
import cv2
capture = cv2.VideoCapture(0)
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])
#H:Hue -->Renk
#S:Saturation -->Doygunluk
#V:Value --> Parlaklık

while(True):
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#BGR den HSV ye dönüşüm sağlandı
    mask = cv2.inRange(hsv, lower_blue, upper_blue)#threshold işlemi uyguladık
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', hsv)#Normal Görüntü
    cv2.imshow('mask', mask)#Siyah beyaz görüntü
    cv2.imshow('res', res)#Siyah mavi Görüntü
    if cv2.waitKey(1) == ord('q'):
        break