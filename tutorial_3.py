import cv2 as cv
import numpy as np

def color_space(src):
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    gray = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", gray)
    gray = cv.cvtColor(src, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", gray)
    gray = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", gray)


def extrace_object():
    capture = cv.VideoCapture("D:/xxx.mp4")
    while True:
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([35,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow('video',frame)
        cv.imshow("MASK",mask)
        c = cv.waitKey(50)
        if c == 27:
            break

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.namedWindow("input_image",cv.WINDOW_NORMAL)
cv.imshow("input_image",src)
color_space(src)
# extrace_object()

b,g,r = cv.split(src)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

src[:,:,2] = 0
# src = cv.merge([b,g,r])
cv.imshow("change",src)
cv.waitKey(0)

cv.destroyAllWindows()