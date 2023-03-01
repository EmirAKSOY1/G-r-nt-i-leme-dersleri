#Tuş Basılma olayı

import cv2 as cv

resim = cv.imread('resim/yol.jpeg',0)
cv.imshow("deneme",resim)
a = cv.waitKey(0)#ASCII değerini verir
print(a)
