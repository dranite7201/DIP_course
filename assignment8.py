import cv2
import numpy as np

img = cv2.imread("images/sudoku.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

b_filter = cv2.bilateralFilter(gray_image,15,25,25)

thresh = cv2.adaptiveThreshold(b_filter,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('original image', img)
cv2.imshow('image', thresh)



cv2.waitKey(0)
cv2.destroyAllWindows()