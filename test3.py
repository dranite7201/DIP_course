import cv2
import numpy as np
img =cv2.imread('images/portrait2.jpg')
img = cv2.resize(img,(300,200))
for i in range(1, 9):
    numofLevel = 2.** i
    LevelGap = 256/numofLevel
    quantizedImg = np.uint8(np.ceil(img/LevelGap)*LevelGap-1)
    cv2.imshow('portrait bit '+str(i), quantizedImg)


cv2.waitKey(0)      
cv2.destroyAllWindows()