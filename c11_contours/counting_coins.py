import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow('Blurred', blurred)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow('Edges', edged)

# RETR_EXTERNAL to retrieve only the outermost contours
# CHAIN_APPRROX_SIMPLE to compress horizontal, vertical, and diagonal segments into
# their endpoints only
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # return contours, hierarchy
print('I count {} coins in this image'.format(len(cnts)))

coins = image.copy()
# -1: draw all the contours
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 3)
cv2.imshow('Coins', coins)

cv2.waitKey()

for i, c in enumerate(cnts):
    x, y, w, h = cv2.boundingRect(c)

    print('Coin #{}'.format(i + 1))
    coin = image[y:y + h, x:x + w]
    cv2.imshow('Coin', coin)

    mask = np.zeros(image.shape[:2], dtype='uint8')
    (center_x, center_y), radius = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(center_x), int(center_y)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    cv2.imshow('Masked Coin', cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey()
