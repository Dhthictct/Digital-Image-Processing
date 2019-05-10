# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import math
import cv2 as cv

src = cv.imread("lena.bmp")
original = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

average3 = cv.blur(original, (3, 3))
average7 = cv.blur(original, (7, 7))

cv.imshow("original image", original)
cv.imshow("3x3 image", average3)
cv.imshow("7x7 image", average7)
cv.waitKey(0)
cv.destroyAllWindows()
