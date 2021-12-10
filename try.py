import cv2
import numpy as np 
import math

img = cv2.imread('images/venice.jpg',0)
h,w = img.shape


x = 3
s = 2
probs = [math.exp(-(2*x*x)/(2*s*s))/2*math.pi*s*s for x in range(-x,x+1)] 
kernel = np.outer(probs, probs)

new_img = np.zeros((h,w))

for i in range(h):
    for j in range(w):
        sum = 0
        for k in np.arange(-s,s+1):
            for l in np.arange(-s,s+1):
                if i+k < 0  or i + k >= h or s + l < 0 or s + l >= w:
                    a = 0
                    w = kernel[s+k][s+l]
                else:
                    a = img[i+k][j+l]
                    w = kernel[s+k][s+l]
            sum += w*a
        new_img[i][j]=sum

cv2.imshow("changed img", new_img)

cv2.waitKey(0)      
cv2.destroyAllWindows()