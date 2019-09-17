import cv2 as cv
import numpy as np

def bi_demo(img):
    dst = cv.bilateralFilter(img,0,100,15)#d=distance,d和sigmaspace和sigmacolor，如果d没输入，就从sigmaspace计算d,/
    # 如果sigmacolor没输入，就从sigmaspace计算sigmacolor
    cv.imshow("bi_demo",dst)

def bii_demo(img):
    dst = cv.pyrMeanShiftFiltering(img,15,10)
    cv.imshow("bi_demo",dst)


print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.imshow("input_image",src)
# bi_demo(src)
bii_demo(src)

cv.waitKey(0)
