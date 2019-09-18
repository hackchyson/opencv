import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

cropped = image[30:84, 182:244]  # y,x because of the row,column order in numpy
cv2.imshow('Face', cropped)

cv2.waitKey(0)
