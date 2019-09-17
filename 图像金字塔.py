import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def pryamid_demo(img):
    level = 3
    temp = img.copy()
    pyramid_imgs = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_imgs.append(dst)
        cv.imshow('dst+%s'%str(i),dst)
        temp = dst.copy()
    return pyramid_imgs

def lapalian_demo(img):
    pyramid_imgs = pryamid_demo(img)
    level = len(pyramid_imgs)
    for i in range(level-1,-1,-1):
        if (i-1) < 0:
            expand = cv.pyrUp(pyramid_imgs[i], dstsize=img.shape[:2])
            lpls = cv.subtract(img, expand)
            cv.imshow('laplas' + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_imgs[i],dstsize=pyramid_imgs[i-1].shape[:2])
            lpls = cv.subtract(pyramid_imgs[i-1],expand)#拉普拉斯金字塔，原图和升维图像的差
            cv.imshow('laplas'+str(i),lpls)



print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/click.jpg")#拉普拉斯算法必须为正方形图片
# cv.imshow("input_image",src)
# pryamid_demo(src)
lapalian_demo(src)
cv.waitKey(0)
