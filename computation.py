# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("subtract_demo", dst)


def logic_demo(m1, m2):
    dst = cv.bitwise_and(m1, m2)
    cv.imshow("and", dst)
    dst = cv.bitwise_or(m1, m2)
    cv.imshow("or", dst)
    dst = cv.bitwise_not(m1)
    cv.imshow("not", dst)


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)


src1 = cv.imread("result.png")
src2 = cv.imread("awr.png")
print(src1.shape)
print(src2.shape)

contrast_brightness_demo(src1, 1.5, 0)

cv.waitKey(0)
cv.destroyAllWindows()

add_demo(src1, src2)
subtract_demo(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()

img = cv.imread("landscape.png")
logic_demo(src1, img)
cv.waitKey(0)
cv.destroyAllWindows()
