import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def backProjection_demo():
    sample = cv.imread("C:/Users/Administrator/Desktop/caps2.bmp")
    target = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    # cv.imshow('sample',sample)
    # cv.imshow('target',target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[20,20],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow('backProjection',dst)

def hist2d_demo(img):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv],[0,1],None,[32,32],[0,180,0,256])#h通道是180,共两个通道
    # hist = np.flipud(hist)
    # cv.imshow('hist',hist)
    plt.imshow(hist,interpolation='nearest')
    plt.title('2D Histogram')
    plt.show()

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
# cv.imshow("input_image",src)
hist2d_demo(src)
# backProjection_demo()
cv.waitKey(0)
