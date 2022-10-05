import cv2 as cv

img = cv.imread('./Photos/cats.jpg')
cv.imshow('Image', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 40, 20)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)