#iki resmi karıştırma
import cv2 # opencv kütüphanesini ekleme
resim = cv2.imread('resim/yaz.jpg') # resim okuma.
resim2 = cv2.imread('resim/kis.jpg') # resim okuma.
toplam = cv2.addWeighted(resim,1,resim2,0.2,0) # iki resmi karıştırma birinci resmin çarpanı 0*4 ikinci resmin çarpanı 0.6 Gama
cv2.imshow('toplam',toplam) # resmi gösterme.
cv2.waitKey()  # gösterilen resmin kapanmasını engelleme. 