import cv2 as cv
import numpy as np

def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            print(ret)
            break

def get_image_into(image):
    print(image.size)
    print(image.dtype)
    print(image.shape)
    src = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    return src


print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/womanhat.bmp")
cv.namedWindow("input_image",cv.WINDOW_NORMAL)
cv.imshow("input_image",src)
src = get_image_into(src)
cv.imwrite("image1.JPG",src)
cv.imshow("output image",src)
video_demo()
cv.waitKey(0)

cv.destroyAllWindows()