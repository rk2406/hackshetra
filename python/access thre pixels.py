import cv2
import numpy as np

img=cv2.imread('image.jpg')

img1=img[100:150,180:250]=(255,255,0)
#print img[100,180]

cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print img.dtype#to print the depth of image i.e.8 bit colorspace

