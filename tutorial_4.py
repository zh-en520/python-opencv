import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add",dst)

def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("sub",dst)

def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply",dst)

def other(m1,m2):
    M1,dev1 = cv.meanStdDev(m1)
    M2,dev2 = cv.meanStdDev(m2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/womanhat.bmp")
src2 = cv.imread("C:/Users/Administrator/Desktop/sailing2.bmp")
# cv.namedWindow("input_image",cv.WINDOW_NORMAL)
# cv.imshow("input_image",src)
print(src.shape)
print(src2.shape)
add_demo(src,src2)
subtract_demo(src,src2)
multiply_demo(src,src2)
other(src,src2)
cv.waitKey(0)

# cv.destroyAllWindows()