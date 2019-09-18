import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

# [1, 0] means right direction
# [0, 1] means up direction
# the third positive value means along the direction (pixels)
# negative means opposite the direction
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))  # width,height
cv2.imshow('Shifted Down and Right', shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Up and Left', shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow('Shifted Down', shifted)

cv2.waitKey(0)
