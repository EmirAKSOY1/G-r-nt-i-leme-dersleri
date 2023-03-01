#Herhangi bir resime ortaya aim ekleme ekleme

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("resim/griyol.jpeg")

yeksen=img.shape[0]//2#Hata vermemesi için tam bölme kullandık 
xeksen=img.shape[1]//2



img=cv2.line(img,(xeksen-20,yeksen),(xeksen+20,yeksen),(255,0,0),5)#yatay

img=cv2.line(img,(xeksen,yeksen-20),(xeksen,yeksen+20),(255,0,0),5)#dik 

plt.imshow(img)
plt.xticks([10,20,40])
plt.yticks([100,200,400])
plt.show()