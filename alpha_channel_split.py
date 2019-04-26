# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


src = cv.imread("Lena.bmp")
cv.imshow("imput image", src)

b, g, r = cv.split(src)
zero = np.zeros(src.shape[:2], np.uint8)

blue = cv.merge([b, zero, zero])
green = cv.merge([zero, g, zero])
red = cv.merge([zero, zero, r])

cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

cv.waitKey(0)
cv.destroyAllWindows()
