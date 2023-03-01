#web cam 

import cv2 
cap =cv2.VideoCapture(0)#Kendi WebCam için


while True:
    ret,frame=cap.read()  #ret başarılı mı değil mi olduğunu tutar frame video için yakaladığı her fotoğraf karesidir
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#videodaki her bir karenin rengini griye çevir
    cv2.imshow("video",gray)#yakalanan her kareyi ekranda göster
    a= cv2.waitKey(1) #videonun hızını belirler ne kdar yüksek olursa fps o kadar düşük olur
    if a ==27 :
        break


cap.release() #yakalanan görüntüleri bırakır
cv2.destroyAllWindows()