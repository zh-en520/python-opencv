import cv2 as cv
import numpy as np

def access_pixels(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            for cc in range(c):
                pv = image[row,col,cc]
                image[row,col,cc] = 255-pv
    cv.imshow("dst",image)

def creat_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow("new_img",img)

def bitwise(image):
    dst = cv.bitwise_not(image)
    cv.imshow("dst",dst)
    m1 = np.ones([3,3],np.uint8)
    m1.fill(1222.388)
    print(m1)
    m2 = m1.reshape([1,9])
    print(m2)
    m3 = np.array([[2,3,4],[4,5,6],[6,7,8]],np.int8)
    m3.fill(1222.388)
    print(m3)

print("-------Hello Python-------")
src = cv.imread("C:/Users/Administrator/Desktop/caps.bmp")
cv.namedWindow("input_image",cv.WINDOW_NORMAL)
cv.imshow("input_image",src)
t1 = cv.getTickCount()
# access_pixels(src)
# creat_image()
bitwise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time:%s ms"%(time*1000))

cv.waitKey(0)

cv.destroyAllWindows()