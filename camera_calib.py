#!/usr/bin/python

import cv2
import numpy
import matplotlib.pyplot as plt
import matplotlib.img as mpimg

img = cv2.imread("./camera_cal/calibration2.jpg")
plt.imshow(img)
exit(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (9,6), None)

ret
