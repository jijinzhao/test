# 导入需要的模块
import os
import cv2
import numpy as np

# 定义一个函数，给图片添加随机的中小雾效果
def add_random_fog(image):
    # 获取图片的宽度和高度
    width, height = image.shape[1], image.shape[0]
    # 生成一个随机的雾度系数，范围在0.1到0.5之间
    fog_coeff = np.random.uniform(0.5, 0.7)
    # 生成一个和图片大小相同的雾层，颜色为白色
    fog_layer = np.ones((height, width, 3), dtype=np.uint8) * 255
    # 将雾层和图片按照雾度系数混合，得到添加随机雾效果的图片
    fogged_image = cv2.addWeighted(image, 1 - fog_coeff, fog_layer, fog_coeff, 0)
    # 返回添加随机雾效果的图片
    return fogged_image

# 定义一个文件夹路径，存放要处理的图片
folder_path = r"F:\DataBase\dataset\Uint\imagesUint"
# 遍历文件夹下的所有文件
for file in os.listdir(folder_path):
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, file)
    # 获取文件的名称和后缀
    file_name, file_ext = os.path.splitext(file)
    # 判断文件是否是.jpg或.jpeg结尾
    if file_ext.lower() in [".jpg", ".jpeg"]:
        # 如果是，读取图片数据
        image = cv2.imread(file_path)
        # 给图片添加随机雾效果
        fogged_image = add_random_fog(image)
        # 保存添加随机雾效果的图片到原来的路径，名称后面加上_fogged
        cv2.imwrite(file_path.replace(file_name, file_name + "_fogged"), fogged_image)
        # 打印出处理成功的信息
        print(f"Added random fog effect to {file}")
    else:
        # 如果不是，打印出该文件的文字和后缀
        print(f"This file is not an image: {file_name}{file_ext}")
