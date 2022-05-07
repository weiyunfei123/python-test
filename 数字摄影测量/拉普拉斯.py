
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
img = cv2.imread('D:\2.jpg')

# 图像向下取样
r1 = cv2.pyrDown(img)

# 图像向上取样
r2 = cv2.pyrUp(r1)

# 拉普拉斯第0层
LapPyr0 = img - r2

# 图像向下取样
r3 = cv2.pyrDown(r1)

# 图像向上取样
r4 = cv2.pyrUp(r3)

# 拉普拉斯第1层
LapPyr1 = r1 - r4

# 显示图像
cv2.imshow('original', img)
cv2.imshow('LapPyr0', LapPyr0)
cv2.imshow('LapPyr1', LapPyr1)
cv2.waitKey()
cv2.destroyAllWindows()