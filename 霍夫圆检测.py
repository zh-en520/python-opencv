import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hough_circle_demo(img):
    # dst = cv.pyrMeanShiftFiltering(img,13,85)
    # dst = cv.GaussianBlur(img,(5,5),25)
    dst = cv.medianBlur(img,13)
    cimg = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,47,param2=47,param1=80,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(img,(i[0],i[1]),2,(255,0,0),2)
    cv.imshow('circles',img)
    cv.imshow('epf',dst)

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/money.png")
# cv.imshow("input_image",src)
hough_circle_demo(src)

cv.waitKey(0)
