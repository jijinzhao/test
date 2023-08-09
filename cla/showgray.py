import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot(grayHist):
    plt.plot(range(256), grayHist, 'r', linewidth=1.5, c='red')
    y_maxValue = np.max(grayHist)
    plt.axis([0, 255, 0, y_maxValue]) # x和y的范围
    plt.xlabel("gray Level")
    plt.ylabel("Number Of Pixels")
    plt.show()

if __name__ == "__main__":
    # 读取图像并转换为灰度图
    img = cv2.imread(r'C:\Users\Administrator\Desktop\test\cla\rs\2.jpg', 0)
    # 图像的灰度级范围是0~255
    grayHist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # 绘制直方图
    plot(grayHist)