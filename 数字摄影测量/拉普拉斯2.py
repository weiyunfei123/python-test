
import cv2


o=cv2.imread("D:/4.jpg") # 读取原始图像

od=cv2.pyrDown(o)# 图像向下取样
odu=cv2.pyrUp(od)# 图像向上取样
lapPyr=o-odu  # 拉普拉斯第0层

o1=od
odd=cv2.pyrDown(o1)
oddu=cv2.pyrUp(odd)
lapPyr1=o1-oddu  # 拉普拉斯第1层

# 显示图像
cv2.imshow("original",o)
cv2.imshow("laplacianPyr0",lapPyr)
cv2.imshow("laplacianPyr1",lapPyr1)
cv2.waitKey()
cv2.destroyAllWindows()