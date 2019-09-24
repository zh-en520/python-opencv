import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def edge_demo(img):  # 边缘提取
    blur = cv.GaussianBlur(img, (3, 3), 0)  # ksize和sigmma只选一个值，可以互相求值
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge_output = cv.Canny(grad_x,grad_y,50,150)
    edge_output = cv.Canny(blur, 50, 150)
    cv.imshow('Canny', edge_output)
    #
    # dst = cv.bitwise_and(img, img, mask=edge_output)
    # cv.imshow('dst', dst)
    return edge_output


def contourse_demo(img):
    # dst = cv.GaussianBlur(img,(9,9),15)
    # gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    # ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    # print(ret)
    # cv.imshow('binary',binary)

    binary = edge_demo(img)

    contours,heriachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    print(heriachy)
    for i,contour in enumerate(contours):
        # cv.drawContours(img,contours,i,(0,0,255),2)
        cv.drawContours(img,contours,i,(0,0,255),-1)#-1是填充
    cv.imshow('contourse',img)



print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/money.png")
cv.imshow("input_image",src)
contourse_demo(src)

cv.waitKey(0)
