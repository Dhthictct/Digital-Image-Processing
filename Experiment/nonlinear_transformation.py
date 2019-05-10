# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import math
import cv2 as cv

src = cv.imread("lena.bmp")
original = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 指数变换
gamma = copy.deepcopy(original)
for i in range(gamma.shape[0]):
    for j in range(gamma.shape[1]):
        gamma[i][j] = 3*pow(gamma[i][j], 0.8)

# 对数变换
logarithm = copy.deepcopy(original)
for i in range(logarithm.shape[0]):
    for j in range(logarithm.shape[1]):
        logarithm[i][j] = 3 * math.log(1 + logarithm[i][j])

cv.imshow("original image", original)
cv.imshow("gamma image", gamma)
cv.imshow("logarithmic image", logarithm)
cv.waitKey(0)
cv.destroyAllWindows()
