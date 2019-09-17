import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#图像梯度是自定义卷积的另一种应用方式，包括锐化，模糊等
#图像梯度是相邻不同像素间的差值的整体效果图
#一阶导数和sobel算子
def sobel_demo(img):
    # grad_x = cv.Sobel(img,cv.CV_32F,1,0)#x方向的梯度，depth如果==8U,可能会导致overflow,超出取值范围255，或者截断，所以用32F
    # grad_y = cv.Sobel(img,cv.CV_32F,0,1)#对y求一阶导，一般源图像都为CV_8U，为了避免溢出，一般ddepth参数选择CV_32F
    #ddepth =-1时，代表输出图像与输入图像相同的深度。
    grad_x = cv.Scharr(img, cv.CV_32F, 1, 0)#sobel算子的增强版
    grad_y = cv.Scharr(img, cv.CV_32F, 0, 1)#sobel算子的增强版
    gradx = cv.convertScaleAbs(grad_x)#结果可能有正有负，取绝对值，将其转到8位的图像上
    grady = cv.convertScaleAbs(grad_y)#用convertScaleAbs()函数将其转回原来的uint8形式
    cv.imshow('grad_x',gradx)
    cv.imshow('grad_y',grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow('gradxy',gradxy)

#二阶导数和拉普拉斯算子
def laplacian_demo(img):
    # dst = cv.Laplacian(img,cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    # #自定义4邻域
    # kernal = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    # dst = cv.filter2D(img,cv.CV_32F,kernal)
    # lpls = cv.convertScaleAbs(dst)
    #自定义8邻域
    kernal = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    dst = cv.filter2D(img,cv.CV_32F,kernal)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('laplacian',lpls)



print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/click.jpg")
cv.imshow("input_image",src)
sobel_demo(src)
# laplacian_demo(src)
cv.waitKey(0)
