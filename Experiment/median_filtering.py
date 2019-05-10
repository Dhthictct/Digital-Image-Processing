# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import cv2 as cv

src = cv.imread("lena.bmp")
original = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
median = cv.medianBlur(original, 3)

cv.imshow("original image", original)
cv.imshow("medianBlur3x3 image", median)
cv.waitKey(0)
cv.destroyAllWindows()
