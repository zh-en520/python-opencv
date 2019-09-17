import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def threshold_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_TRIANGLE)#三角阈值法适合用在有单个波峰的图像
    # ret,binary = cv.threshold(gray,127,255,cv.THRESH_TRUNC)
    # ret,binary = cv.threshold(gray,127,255,cv.THRESH_TOZERO)
    print('ret',ret)
    cv.imshow('binary',binary)

#局部二值化可以很好的显示作文，文章等，提取字体
def local_threshold(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,25,10)#blocksize必须是奇数，C是常量。
    # 如果当前像素和均值的差小于C，就怎样怎样
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    cv.imshow('binary',binary)


def custom_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    m = np.reshape(gray,[1,w*h])
    mean = m.sum() / (w*h)
    print(mean)
    ret,binary = cv.threshold(gray,mean,255,cv.THRESH_BINARY)
    print(ret)
    cv.imshow('binary',binary)



print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.imshow("input_image",src)
# threshold_demo(src)
# local_threshold(src)
custom_demo(src)
cv.waitKey(0)
