#resime daire ekleme
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("resim/griyol.jpeg")

img = cv2.circle(img,(350,350),20,(255,0,0),3)#20 Yarıçap

plt.imshow(img)
plt.xticks([10,20,40])
plt.yticks([100,200,400])
plt.show()