import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def big_image_demo(img):
    cw = 25
    ch = 25
    h,w = img.shape[:2]
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    for row in range(0,h,cw):
        for col in range(0,w,ch):
            roi = gray[row:row+ch,col:col+cw]
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 15:
                gray[row:row+ch,col:col+cw] = 0#roi与空白区域过滤
            else:

                ret,dst =  cv.threshold(roi,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)#全局阈值的方法OTSU对局部噪声会\
                # 生成不必要的二值化
                # dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,10)
                gray[row:row+ch,col:col+cw] = dst

    cv.imwrite('binary.jpg',gray)


print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.imshow("input_image",src)
big_image_demo(src)

cv.waitKey(0)
