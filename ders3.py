import cv2 as cv

resim = cv.imread("resim/yol.jpeg")


cv.imshow("deneme", resim)#resmi ekranda gösterir
cv.waitKey(0)#ms cinsinden bekler eğer 0 yazarsan bir tuşa basınca kapanır.
cv.destroyAllWindows()#pencereyi kapatır olsa da olur olmasa da 
