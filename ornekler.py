
import cv2
import math
import numpy as np
import time
scale=25
lower_red = np.array([100, 110, 110])
upper_red = np.array([130, 255, 255])
kilit=False
video=cv2.VideoCapture(0)
i=True

while i:
    success, img=video.read()
    img=cv2.flip(img,1)
    """
    Zoom lu Görüntü
    zoomheight,zoomwidth, zoomchannels = img.shape
    centerX,centerY=int(zoomheight/2),int(zoomwidth/2)
    radiusX,radiusY= int(scale*zoomheight/100),int(scale*zoomwidth/100)

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    cropped = img[minX:maxX, minY:maxY]
    img= cv2.resize(cropped, (zoomwidth, zoomheight)) 


    """

    image=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    mask=cv2.inRange(image,lower_red,upper_red)
    
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    mask=cv2.bitwise_and(img,img,mask=mask)
   

    #aim
    img=cv2.line(img, (300,250),(320,250),(0,0,0),1)
    img=cv2.line(img, (310,240),(310,260),(0,0,0),1)
    #/aim

    if len(contours)!=0:
        
        for contour in contours:
            
            if cv2.contourArea(contour)>2000:
                
                
                x,y,w,h=cv2.boundingRect(contour)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
               
                img=cv2.line(img,(x,y),(x+w,y+h),(0,255,0),1)
                img=cv2.line(img,(x+w,y),(x,h+y),(0,255,0),1)
                yariw=w/2
                yarix=int(x+yariw)
                yarih=h/2
                yariy=int(y+yarih)
                cv2.circle(img,(yarix,yariy),6,(255,255,255),-1)
                img=cv2.line(img, (310,250),(yarix,yariy),(255,255,255),1)
                x=math.pow((310-yarix),2)+math.pow((250-yariy),2)
                x=math.sqrt(x)
                #print("Öndekine Çakabilirim x=>",yarix-310," y=> ",yariy-250)
                # while yarix>30:
                #     print("sağa dönülüyor")
                #     time.sleep(1)
                    
                    
                if(x<30):
                    pass
                    #print("Hedef Vuruldu")
                    
                #     i=False
                #     print("Mekanizma Çalıştı")
    else:
        print("yok")       
    #cv2.imshow("mask",mask)
                
    cv2.imshow("cam",img)
    k=cv2.waitKey(1)
    if k==27:
        break
    
video.release()
cv2.destroyAllWindows()  