import cv2 as cv
img = cv.imread("lena.jpg")
cv.imshow("Image",img)
cv.waitKey(0)