import cv2
cap=cv2.VideoCapture(0)
car_cascade=cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
font=cv2.FONT_HERSHEY_SIMPLEX
i=0
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    arabalar=car_cascade.detectMultiScale(frame,1.1,6)

    for(x,y,w,h) in arabalar:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        i+=1

    #yazi=cv2.putText(frame,str(i),(10,100),font,2,(0,255,0),2)
    cv2.imshow("frame",frame)

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()