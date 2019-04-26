# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


src = cv.imread("lena.bmp")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)
cv.destroyAllWindows()
