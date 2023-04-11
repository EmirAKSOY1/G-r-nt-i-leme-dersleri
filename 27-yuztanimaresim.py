import cv2

import numpy as np

face_cascade=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")#xml dosyasını dahil ettik

imge=cv2.imread("resim/insanlar.png")

gray=cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)#renk dönüşümü yaptık
faces=face_cascade.detectMultiScale(gray,1.1,4)#yakaladığımız görüntülerin kooardinatlarını tutar 

i=0
for(x,y,w,h) in faces:
    cv2.rectangle(imge,(x,y),(x+w,y+h),(0,0,255),1)#O koordinattaki yüzleri kare içerisine alır.
    i+=1
print(i)
imge=cv2.putText(imge,f"Resimde {i} Kisi var",(150,350),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)#Resimde kaç kişi var bulmak için
cv2.imshow("deneme",imge)

cv2.waitKey(0)