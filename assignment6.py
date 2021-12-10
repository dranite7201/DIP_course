import cv2
import numpy as np 
def zero_x():
    gray_img = cv2.imread('images/cameraman.tif')

    blur_img = cv2.GaussianBlur(gray_img,(9,9),0)
    LoG = cv2.Laplacian(blur_img, cv2.CV_64F,ksize=3)

    minLoG = cv2.morphologyEx(LoG, cv2.MORPH_ERODE, np.ones((3,3))) 
    maxLoG = cv2.morphologyEx(LoG, cv2.MORPH_DILATE, np.ones((3,3)))  

    zeroCross = np.logical_or(np.logical_and(minLoG < 0,  LoG > 0), np.logical_and(maxLoG > 0, LoG < 0))

    z_c_norm = zeroCross/zeroCross.max()*255
    z_c_image = np.uint8(z_c_norm)

    cv2.imshow('log', z_c_image)
def canny():
    img = cv2.imread('images/venice.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h,w) = gray_img.shape
    h = int(h/2)
    w = int(w/2)
    d = (w,h)
    gray_img = cv2.resize(gray_img,d,interpolation=cv2.INTER_AREA)
    sigma = [np.sqrt(2), np.sqrt(8), np.sqrt(32)]
    print(sigma)
    for s in sigma:
        blured = cv2.GaussianBlur(gray_img,(3,3),s)
        canny_img = cv2.Canny(blured,75, 200)
        cv2.imshow('canny with sigma ' + str(s), canny_img)

zero_x()

cv2.waitKey(0)
cv2.destroyAllWindows()

    