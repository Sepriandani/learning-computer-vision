import numpy as np
import cv2 as cv

# Read image
img = cv.imread ( 'Photos/cat_large.jpg' )
cv.imshow ( 'gambar' , img )
cv.waitKey (0)