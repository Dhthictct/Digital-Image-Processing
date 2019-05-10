# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import cv2 as cv
import numpy as np

src = cv.imread("lena.bmp")
original = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
negative = copy.deepcopy(original)

for i in range(negative.shape[0]):
    for j in range(negative.shape[1]):
        negative[i][j] = 255-negative[i][j]

cv.imshow("original image", original)
cv.imshow("negative image", negative)
cv.waitKey(0)
cv.destroyAllWindows()
