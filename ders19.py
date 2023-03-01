#resime yazı ekleme

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("resim/griyol.jpeg")
font = cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'Selam',(150,150),font,3,(255,0,0),5)#3 fONT 5 kalılık

plt.imshow(img)
plt.xticks([10,20,40])
plt.yticks([100,200,400])
plt.show()