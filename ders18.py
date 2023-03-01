#resime kare ekleme

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("resim/griyol.jpeg")

img=cv2.rectangle(img,(100,500),(300,700),(255,0,0),5)

plt.imshow(img)
plt.xticks([10,20,40])
plt.yticks([100,200,400])
plt.show()