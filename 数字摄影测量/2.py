# 作者：WeiYunfei
# 时间 2022/3/9 22:12

import numpy as np
import cv2

img = cv2.imread("/home/lisa/dataset/HandDataSet_720_1280/lisa/image/0.jpg", 1)
cv2.imshow("temp", img)
cv2.waitKey(0)

img90 = np.rot90(img)

cv2.imshow("rotate", img90)
cv2.waitKey(0)