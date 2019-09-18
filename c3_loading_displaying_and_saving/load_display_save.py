import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print('width: {} pixels'.format(image.shape[1]))  # notice
print('height: {} pixels'.format(image.shape[0]))
print('channels: {}'.format(image.shape[2]))

cv2.imshow('Image', image)
cv2.waitKey(0)

# OpenCV automatically convert PNG to JPG
cv2.imwrite('newimage.jpg', image)
