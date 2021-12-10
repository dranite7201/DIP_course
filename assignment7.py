import cv2
import numpy as np

img = cv2.imread('images/GetImage.jpeg')
(h,w,c) = img.shape
h = int(h/4)
w = int(w/4)
d = (w,h)

img = cv2.resize(img, d ,interpolation=cv2.INTER_AREA)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

b_img = cv2.Canny(gray_img,50,150,apertureSize = 3)
    
lines = cv2.HoughLines(b_img,1,np.pi/180,50)
aver_theta = []
for rho,theta in lines[0]:
    aver_theta.append(theta)
d = np.abs(90 - (np.median(aver_theta)*180/np.pi))

center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,d , 1.0)
rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
cv2.imshow('image',img)
cv2.imshow('rotated',rotated)



cv2.waitKey(0)
cv2.destroyAllWindows()