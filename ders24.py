#zoom lu goruntu

import cv2 
cap =cv2.VideoCapture(0)#Kendi WebCam için
scale=25
while True:
    ret,frame=cap.read()  #ret başarılı mı değil mi olduğunu tutar frame video için yakaladığı her fotoğraf karesidir

    zoomheight,zoomwidth, zoomchannels = frame.shape
    centerX,centerY=int(zoomheight/2),int(zoomwidth/2)
    radiusX,radiusY= int(scale*zoomheight/100),int(scale*zoomwidth/100)

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    cropped = frame[minX:maxX, minY:maxY]
    img= cv2.resize(cropped, (zoomwidth, zoomheight)) 

    cv2.imshow("video",frame)#yakalanan her kareyi ekranda göster
    cv2.imshow("zooum",img)#yakalanan her kareyi ekranda göster
    a= cv2.waitKey(1) #videonun hızını belirler ne kdar yüksek olursa fps o kadar düşük olur

    if a ==27 :
        break

cap.release() #yakalanan görüntüleri bırakır
cv2.destroyAllWindows()