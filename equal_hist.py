# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


src = cv.imread("Lena.bmp")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
equalHist_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
