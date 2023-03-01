#esc ye basıldığında çıkar s ye basıldığında kaydeder

import cv2 as cv

resim = cv.imread('resim/yol.jpeg',0)#resim griye çevrildi
cv.imshow("deneme",resim)
a = cv.waitKey(0)

if a == 27:    #esc ye basıldığında çıkar s ye basıldığında kaydeder
    cv.destroyAllWindows()

elif a == ord('s'):#Klavyed basılan tuşu ifade eder
    cv.imwrite('resim/kayit.jpeg',resim)