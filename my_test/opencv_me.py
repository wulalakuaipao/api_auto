#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2020/1/13 16:27
import cv2
import numpy as np
'''Python给照片换底色(蓝底换红底)
opencv是一个基于BSD许可发行（也就是俗称的开源）的跨平台计算机视觉库，可以运行在Linux、Windows、Android和Mac OS上。
由一系列 C 函数和少量 C++ 类构成的它轻量且高效，并提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视
觉方面的很多通用算法。
对于python而言，在引用opencv库的时候需要写为import cv2。其中，cv2是opencv的C++命名空间名称，
使用它来表示调用的是C++开发的opencv的接口。
'''
img = cv2.imread('timg.jpg')
# img1 = cv2.imread('timg1.jpg')
print(img.shape)
# print(img1.shape)
# 缩放
rows, cols, channels = img.shape
img = cv2.resize(img, None, fx=0.5, fy=0.5)
rows, cols, channels = img.shape
# cv2.imshow('img', img)
# 转换hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([90, 70, 70])
upper_blue = np.array([110, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# cv2.imshow('Mask', mask)
# 腐蚀膨胀
erode = cv2.erode(mask, None, iterations=1)
cv2.imshow('erode', erode)
dilate = cv2.dilate(erode, None, iterations=1)
# cv2.imshow('dilate', dilate)

# 遍历替换
for i in range(rows):
    for j in range(cols):
        if dilate[i, j] == 255:
            img[i, j] = (0, 0, 255)  # 此处替换颜色，为BGR通道
# cv2.imshow('res', img)
img = cv2.resize(img, None, fx=2, fy=2)
rows, cols, channels = img.shape
cv2.imwrite('timg1.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()