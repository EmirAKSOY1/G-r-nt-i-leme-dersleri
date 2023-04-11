#resimde istenen pikselin hsv değerlerini bulma
import cv2
from cv2 import pyrDown
import numpy as np
def TiklamaOlayi(olay, x, y, flags, param):
    
    if olay == cv2.EVENT_LBUTTONDOWN:#Eğer sol click yapıldıysa 
        
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]# o koordinattaki değerleri verir"
        v = hsv[y, x, 2]

        hsvUzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)#Görüntüde istenen değerleri yazdırıyoruz
        cv2.putText(goruntu, hsvUzayi, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (100,20,0),1 )#görüntüye hsv değerlerini eklemeye yarar
        cv2.imshow("Goruntu", goruntu)#tıklamadan sonra görüntüyü yeniler


goruntu = cv2.imread('resim/yaz.jpg') 
goruntu=pyrDown(goruntu)# Görüntüyü küçük pencerede açar

hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)# hsv ye dönüştürülmüş hali

cv2.imshow("Goruntu", goruntu)

cv2.setMouseCallback('Goruntu',TiklamaOlayi)# resmin tıklanma olayı

cv2.waitKey(0)
cv2.destroyAllWindows()