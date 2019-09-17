import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def template_demo():
    tpl = cv.imread("C:/Users/Administrator/Desktop/caps2.bmp")
    target = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCOEFF_NORMED,cv.TM_CCORR_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc#topleft
        br = (tl[0]+tw,tl[1]+th)#bownten_right
        cv.rectangle(target,tl,br,(0,0,255),2)
        cv.imshow('match-%s' % str(md),result)
        # cv.imshow('match-%s' % str(md),target)

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
# cv.imshow("input_image",src)
template_demo()

cv.waitKey(0)
