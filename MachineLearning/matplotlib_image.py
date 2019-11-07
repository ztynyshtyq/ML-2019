import cv2
from matplotlib import pyplot as plt
img = cv2.imread('imgs/butterfly.jpg', 1)

plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
