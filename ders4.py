#Gri Resim

import cv2 as cv


#resim = cv.imread("resim/yol.jpeg", cv.IMREAD_GRAYSCALE) 
resim = cv.imread("resim/yol.jpeg", 0) #Buda Gri Yapar


cv.imshow("deneme", resim)
cv.waitKey(1000)#ms cinsinden bekler eğer 0 yazarsan bir tuşa basınca kapanır.

print(resim)