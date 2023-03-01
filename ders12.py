#piksel okuma
import cv2 as cv

resim = cv.imread("resim/yol.jpeg")


cv.imshow("deneme", resim)
print(resim[0,0])
cv.waitKey(0)#ms cinsinden bekler eğer 0 yazarsan bir tuşa basınca kapanır.
cv.destroyAllWindows()#pencereyi kapatır olsa da olur olmasa da 
print(resim)