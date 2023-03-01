#Resim kaydetme

import cv2 as cv

resim = cv.imread('resim/yol.jpeg',0)
cv.imshow("deneme",resim)
cv.imwrite("resim/griyol.jpeg",resim)
