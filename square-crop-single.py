imprt os
import cv2
#import numpy as np

# read image
img = cv2.imread('test.JPG')
height, width, channels = img.shape

# new position for square image cropping
upper_left = (int((width - height) / 2), 0)
bottom_right = (int((width + height) / 2), height)

# crop and write the cropped image to disk in jpg format
img_crop = img[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]]
cv2.imwrite('test2.jpg', img_crop)

'''
# view crop image in window. default WINDOW_AUTOSIZE
cv2.namedWindow('crop', cv2.WINDOW_NORMAL)
cv2.imshow('crop', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''




