# 导入os模块和PIL模块
import os
from PIL import Image

# 定义图片文件夹的路径
image_folder = r"F:\DataBase\night\picsPro"
# 定义一个计数器，用于重命名图片
count = 512

# 遍历文件夹中的所有文件
for file in os.listdir(image_folder):
    # 获取文件的完整路径
    file_path = os.path.join(image_folder, file)
    # 判断文件是否是图片，通过尝试打开文件并获取其格式
    try:
        # 打开文件并获取格式
        image_format = Image.open(file_path).format
        # 如果是图片，打印文件名和格式，并重命名图片
        print(f"{file} is an image with format {image_format}.")
        # 生成新的文件名，使用计数器和原来的格式
        new_file_name = f"{count}.{image_format.lower()}"
        # 生成新的文件路径
        new_file_path = os.path.join(image_folder, new_file_name)
        # 重命名图片
        os.rename(file_path, new_file_path)
        # 打印重命名后的文件名
        print(f"Renamed {file} to {new_file_name}.")
        # 计数器加一
        count += 1
    # 如果不是图片，打印文件名和错误信息，并跳过该文件
    except IOError:
        print(f"{file} is not an image. Skipped.")
