#matplotlib kullanarak resim gösterme

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("resim/griyol.jpeg")



plt.imshow(img)
plt.xticks([10,20,40])
plt.yticks([100,200,400])
plt.show()