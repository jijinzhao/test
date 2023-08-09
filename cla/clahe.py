import cv2 # 导入OpenCV库
from matplotlib import pyplot as plt # 导入matplotlib库的pyplot模块
import time # 导入time库

tic = time.time() # 记录开始时间
image = cv2.imread(r'C:\Users\Administrator\Desktop\test\cla\2.jpg', cv2.IMREAD_COLOR) # 以彩色模式读取图片
b, g, r = cv2.split(image) # 将图片分割为三个通道
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) # 创建一个CLAHE对象，设置裁剪限制为2.0，网格大小为8x8
b = clahe.apply(b) # 对蓝色通道应用CLAHE
g = clahe.apply(g) # 对绿色通道应用CLAHE
r = clahe.apply(r) # 对红色通道应用CLAHE
image = cv2.merge([b, g, r]) # 将三个通道合并为一个图片
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)  # 将RGB图像转换为YCbCr空间中
Y = ycrcb[:, :, 0] # 提取亮度分量
hist = cv2.calcHist([Y], [0], None, [256], [0, 255]) # 计算亮度分量的直方图
toc = time.time() # 记录结束时间
print('Using time is', toc - tic) # 打印使用时间
plt.plot(hist, 'k') # 用黑色线条绘制直方图
plt.show() # 显示绘制的图像
cv2.imshow(r'clbd.jpg', image) # 显示经过CLAHE处理的图片
cv2.imwrite(r'C:\Users\Administrator\Desktop\test\cla\rs\2.jpg', image) # 将处理后的图片保存到指定路径
cv2.waitKey(0) # 等待用户按键
cv2.destroyAllWindows() # 销毁所有窗口
