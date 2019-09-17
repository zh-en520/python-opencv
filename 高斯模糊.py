import cv2 as cv
import numpy as np

def clamp(pv):
    if pv < 0:
        pv = 0
    elif pv > 255:
        pv = 255
    return pv

def guassian_nosie(img):
    h,w,c = img.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = img[row,col,0]
            g = img[row,col,1]
            r = img[row,col,2]
            img[row,col,0] = clamp(b+s[0])
            img[row,col,1] = clamp(g+s[1])
            img[row,col,2] = clamp(r+s[2])
    cv.imshow('noise',img)
    dst = cv.GaussianBlur(img, (5, 5), 15)#15==sigmaa,sigmaa可以在公式中和x互相计算得到，ksize为0时，使用sigmaa计算高斯模糊
    cv.imshow('dst', dst)



print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")

cv.imshow("input_image",src)
t1 = cv.getTickCount()
guassian_nosie(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print('time consume:%s' % (time*1000))
cv.imshow('src',src)

cv.waitKey(0)
