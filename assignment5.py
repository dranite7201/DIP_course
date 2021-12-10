import numpy as np
import cv2
import random
import math

img = cv2.imread("images/cell.tif")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#generate gray noise image
rows, columns = img_gray.shape
p = 0.05
img_gray_noise = np.zeros(img_gray.shape, np.uint8)

for i in range(rows):
    for j in range(columns):
        r = random.random()     
        if r < p/2:
            img_gray_noise[i][j] = 0
        elif r < p:
            img_gray_noise[i][j] = 255
        else:
            img_gray_noise[i][j] = img_gray[i][j]

def new_media_filter(img_gray_noise,n,thresh):
    new = cv2.medianBlur(img_gray_noise,n)
    old = np.float64(img_gray_noise)
    new = np.float64(new)
    for i in range (rows):
        for j in range (columns):
            if np.abs(old[i][j]-new[i][j]) <= thresh:
                new[i][j] = old [i][j]
    new = np.array(new,dtype=np.uint8)
    return new
denoise_img = new_media_filter(img_gray_noise,3,50)
cv2.imshow('denoised image', denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows
    