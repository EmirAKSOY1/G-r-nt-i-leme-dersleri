import cv2
import numpy as np

img = cv2.imread('resim/yol.jpeg')

median = cv2.medianBlur(img, 11)
Blur = cv2.GaussianBlur ( median , ( 11 , 11 ) , cv2.BORDER_DEFAULT )
img=cv2.Canny(Blur,50,10)
cv2.imshow('img2', median)
cv2.imshow('img', img)
cv2.imshow('img3', Blur)

cv2.waitKey(0)
cv2.destroyAllWindows()