import cv2
import matplotlib.pyplot as plt
img = cv2.imread('flower.jpeg')
blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(blur)
plt.show()