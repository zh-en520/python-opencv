import cv2 as cv
import numpy as np

def equalHist_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('dst',dst)

def clahe_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = clahe.apply(gray)
    cv.imshow('dst', dst)

def create_rgb(img):
    h,w,c = img.shape
    rgbHist = np.zeros([8*8*8,1],np.float32)
    bsize = 256/8
    for row in range(h):
        for col in range(w):
            b = img[row,col,0]
            g = img[row,col,1]
            r = img[row,col,2]
            index = np.int(b/bsize)*8*8+np.int(g/bsize)*8+np.int(r/bsize)
            rgbHist[np.int(index),0] += 1
    return rgbHist

def hist_compare(img1,img2):
    hist1 = create_rgb(img1)
    hist2 = create_rgb(img2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match4 = cv.compareHist(hist1, hist2, cv.HISTCMP_INTERSECT)
    print('巴氏距离：%s,卡方：%s,相关性：%s,内：%s' % (match1,match2,match3,match4))

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
src2 = cv.imread("C:/Users/Administrator/Desktop/sailing2.bmp")
cv.imshow("input_image",src)
# equalHist_demo(src)
clahe_demo(src)
# hist_compare(src,src2)

cv.waitKey(0)
