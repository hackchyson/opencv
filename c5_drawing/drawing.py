import numpy as np
import cv2

# line and rectangle
# Since we are representing our image as an RGB image with pixels in the range [0, 255]
# it's important that we use an 8-bit unsigned integer, or uint8
canvas = np.zeros((300, 300, 3), dtype='uint8')

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)  # (x, y)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)  # top-left, bottom-right
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)  # -1 stands for filled
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# circle
canvas = np.zeros((300, 300, 3), dtype='uint8')
center_x, center_y = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (center_x, center_y), r, white)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, 200)
    color = np.random.randint(0, 256, (3,)).tolist()
    center = np.random.randint(0, 300, (2,))
    cv2.circle(canvas, tuple(center), radius, color, -1)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
