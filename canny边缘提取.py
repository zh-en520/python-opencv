import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#输入彩色图像，高斯模糊，去噪声，求取梯度，根据图像角度实现非最大信号压制，进行高低阈值的过滤，输出二值图像，得到边缘
#即：高斯模糊、灰度转换、计算梯度、非最大信号抑制、高低阈值输出二值图像

def edge_demo(img):
    blur = cv.GaussianBlur(img,(3,3),0)#ksize和sigmma只选一个值，可以互相求值
    gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray,cv.CV_16SC1,1,0)
    grad_y = cv.Sobel(gray,cv.CV_16SC1,0,1)
    # edge_output = cv.Canny(grad_x,grad_y,50,150)
    edge_output = cv.Canny(blur,50,150)
    cv.imshow('Canny',edge_output)

    dst = cv.bitwise_and(img,img,mask=edge_output)
    cv.imshow('dst',dst)


print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.imshow("input_image",src)
edge_demo(src)

cv.waitKey(0)
