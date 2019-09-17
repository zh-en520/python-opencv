import cv2 as cv
import numpy as np

def blur_demo(img):#均值模糊
    dst = cv.blur(img,(5,5))
    cv.imshow('123',dst)

def median_demo(img):#中值模糊
    dst = cv.medianBlur(img, 5)
    cv.imshow('123', dst)

def custom_demo(img):#自定义模糊
    kernal = np.ones([5,5],np.float32)/25
    dst = cv.filter2D(img,-1,kernal)
    cv.imshow('123', dst)

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")

cv.imshow("input_image",src)
# blur_demo(src)
# median_demo(src)
custom_demo(src)
cv.waitKey(0)
