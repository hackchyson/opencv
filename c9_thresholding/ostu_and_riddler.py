import numpy as np
import argparse
import cv2
import mahotas

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)  # remove some of high frequency edges
cv2.imshow('Image', image)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Otsu', thresh)

T = mahotas.thresholding.rc(blurred)
print('Riddler-Calvard: {}'.format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Riddle-Calvard', thresh)

# I think this is simpler
T, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('OpenCV Otsu threshold', thresh)

cv2.waitKey()
