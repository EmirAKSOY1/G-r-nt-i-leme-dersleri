#Görüntüdeki Beyaz yerleri bulma

import cv2 as cv
import numpy as np

resim = cv.imread("resim/yol.jpeg") #Buda Gri Yapar

lower_white = np.array([0,0,240])
upper_white = np.array([255,240,255])

hsv = cv.cvtColor(resim, cv.COLOR_BGR2HSV)
mask=cv.inRange(hsv,lower_white,upper_white)

contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(resim, contours, -1, (0, 255, 0), 3)

cv.imshow("deneme", resim)
cv.waitKey(0)#ms cinsinden bekler eğer 0 yazarsan bir tuşa basınca kapanır.

