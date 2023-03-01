#video oynatma


import cv2 
cap =cv2.VideoCapture("resim/yol.mp4")


while True:
    ret,frame=cap.read()  #ret başarılı mı değil mi olduğunu tutar frame video için yakaladığı her fotoğraf karesidir
    cv2.imshow("video",frame)#yakalanan her kareyi ekranda göster
    a= cv2.waitKey(5) #videonun hızını belirler ne kdar yüksek olursa fps o kadar düşük olur
    if a ==27 :
        break


cap.release() #yakalanan görüntüleri bırakır
cv2.destroyAllWindows()