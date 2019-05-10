# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import cv2 as cv

src = cv.imread("lena.bmp")
original = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img = cv.bilateralFilter(original, 40, 75, 75)
lap = cv.Laplacian(img, cv.CV_16S, ksize=3)
dst = cv.convertScaleAbs(lap)
result = copy.deepcopy(original)

for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        result[i][j] = (result[i][j]+dst[i][j]) % 256

cv.imshow("original image", original)
cv.imshow("laplacian image", result)
cv.waitKey(0)
cv.destroyAllWindows()
