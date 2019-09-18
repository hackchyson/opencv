import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

b, g, r = image[0, 0]
print('Pixel at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))

image[0, 0] = (0, 0, 255)
b, g, r = image[0, 0]
print('Pixel at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))

corner = image[0:100, 0:50]
cv2.imshow('Corner', corner)

# height, width because of the row, column representation in numpy
image[0:100, 0:50] = (0, 255, 0)
cv2.imshow('Updated', image)

cv2.waitKey(0)
