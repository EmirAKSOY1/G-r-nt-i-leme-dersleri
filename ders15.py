#resim çevirme 


import cv2 as cv

resim = cv.imread("resim/yaz.jpg")

yeni_resim = cv.flip(resim, 2)#-1,0,1 ,2

cv.imshow("a", yeni_resim)
cv.waitKey(0)