
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import math


# 读取图片
imageyuantu = cv2.imread(r"D:\bingdundun.jpg")

# 图片缩放
imagesuofang = cv2.resize(imageyuantu, (0,0),fx=1.5,fy=1.5)

# 图片显示
cv2.imshow("resize", imagesuofang)
cv2.imshow("image", imageyuantu)

cv2.imwrite(r'img1.jpg',imagesuofang)

# 等待窗口
cv2.waitKey(0)
cv2.destroyAllWindows()