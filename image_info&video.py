# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np


def video_demo(video):
    capture = cv.VideoCapture(video)  # video为0打开摄像头
    flip = False
    while(True):
        ret, frame = capture.read()
        if flip:
            frame = cv.flip(frame, 1)
            # flipCode==0垂直翻转（沿X轴翻转），flipCode>0水平翻转（沿Y轴翻转）
            # flipCode<0水平垂直翻转（先沿X轴翻转，再沿Y轴翻转，等价于旋转180°）
        cv.imshow("video", frame)
        c = cv.waitKey(30)
        if c == 13:  # 按下回车键
            flip = not flip
        if c == 27:  # 按下Esc键
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


print("-------- Hello Python --------")
src = cv.imread("Lena.bmp")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
cv.waitKey(0)


gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("result.png", gray)
cv.imshow("input image", gray)
cv.waitKey(0)
cv.destroyAllWindows()
video_demo("video.flv")
