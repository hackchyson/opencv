import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)

# why float64?
# Transitioning from black-to-white is considered a positive
# slope, whereas a transition from white-to-black is a negative slope.
# an 8-bit unsigned integer does not represent negative values.
# Either it will be clipped to zero if you are using OpenCV
# or a modulus operation will be performed using NumPy.
# The short answer here is that if you don’t use a floating
# point data type when computing the gradient magnitude
# image, you will miss edges, specifically the white-to-black
# transitions.
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian', lap)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)
# cv2.imshow('Sobel X without absolute', np.uint8(sobel_x))
# cv2.imshow('Sobel X without All', sobel_x)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey()
