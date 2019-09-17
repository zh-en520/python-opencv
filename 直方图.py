import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(img):
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

def img_hist(img):
    color = ['blue','green','red']
    for i,c in enumerate(color):
        hist = cv.calcHist(img,[i],None,[256],[0,255])
        plt.plot(hist,color=c)
        plt.xlim([0,256])
    plt.show()

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.imshow("input_image",src)
# plot_demo(src)
img_hist(src)
cv.waitKey(0)
