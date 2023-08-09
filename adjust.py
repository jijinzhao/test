# 导入所需的模块
import os
import shutil
from PIL import Image

# 定义图片和xml文件的路径
image_path = r"F:\DataBase\dataset\Uint\imagesUint3"
xml_path = r"F:\DataBase\dataset\Uint\xmlUint3"

# 遍历图片文件夹，判断是否为图片，如果是则检查是否有对应的xml，否则删除
for file in os.listdir(image_path):
    file_path = os.path.join(image_path, file)
    try:
        # 尝试打开文件为图片，如果成功则为图片，否则为其他类型的文件
        Image.open(file_path)
        # 获取图片文件名的前缀部分
        image_prefix = os.path.splitext(file)[0]
        # 拼接xml文件的路径
        xml_file = os.path.join(xml_path, image_prefix + ".xml")
        # 判断xml文件是否存在，如果不存在则删除图片
        if not os.path.exists(xml_file):
            os.remove(file_path)
    except:
        # 如果打开失败，则跳过该文件
        continue
