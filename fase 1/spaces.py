import cv2 as cv
from cv2 import imshow
import matplotlib.pyplot as plt

img = cv.imread('./Photos/park.jpg')
cv.imshow('Image', img)

# plt.imshow(img)
# plt.show()


# BGR to Graycle
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGRR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
imshow('HSV to BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)