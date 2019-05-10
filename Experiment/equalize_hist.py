# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import cv2 as cv

src = cv.imread("lena.bmp")
original = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(original)

cv.imshow("original image", original)
cv.imshow("equal hist image", dst)
cv.waitKey(0)
cv.destroyAllWindows()
