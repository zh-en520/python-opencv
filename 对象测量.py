import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def measure_object(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    print('ret:',ret)
    cv.imshow('binary',binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    contours,hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])#轮廓面积
        x,y,w,h = cv.boundingRect(contours[i])#轮廓外接矩形四个点
        rate = min(w,h)/max(w,h)
        print('rate:',rate)#可以根据宽高衡重比确定、筛选形状特征，从而确定、减少某些形状圈定
        # print('rect:',rect)
        mm = cv.moments(contours[i])#几何距
        # print('mm:',mm)
        if mm['m00']:
            cx = mm['m10'] / mm['m00']
            cy = mm['m01'] / mm['m00']
        else:
            continue

        cv.circle(dst,(np.int(cx),np.int(cy)),2,(0,0,255),-1)
        # cv.rectangle(dst,(x,y),(x+w,y+h),(0,255,0),2)
        print('area:',area)
        approxCurve = cv.approxPolyDP(contours[i],4,True)
        print('approx:',approxCurve.shape)
        if approxCurve.shape[0] > 7:
            cv.drawContours(dst,contours,i,(0,255,0),2)
        elif approxCurve.shape[0] == 4:
            cv.drawContours(dst,contours,i,(255,0,0),2)
        elif approxCurve.shape[0] == 3:
            cv.drawContours(dst,contours,i,(0,0,255),2)
        elif approxCurve.shape[0] == 2:
            cv.drawContours(dst,contours,i,(10,100,20),2)
    cv.imshow('measure_contours',dst)



print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/jihe.jpg")
cv.imshow("input_image",src)
measure_object(src)

cv.waitKey(0)
