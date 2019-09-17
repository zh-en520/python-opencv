import cv2 as cv
import numpy as np

def fill_color(image):
    copyimg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyimg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("123",copyimg)

def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255

    cv.imshow("123",image)
    mask = np.zeros([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("234", image)

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")

# cv.imshow("change",src)
# face = src[50:250,100:300]
# gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
# back = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
# src[50:250,100:300] = back
# cv.imshow("face",src)
# fill_color(src)
fill_binary()
cv.waitKey(0)
