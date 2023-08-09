# 导入os模块
import os

# 定义图片和xml文件的路径
image_path = r"F:\DataBase\dataset\Uint\imagesUint2"
xml_path = r"F:\DataBase\dataset\Uint\xmlUint2"

# 遍历图片文件夹，判断是否为.jpg或.JPEG格式，如果不是则删除该文件，同时删除对应的xml文件
for file in os.listdir(image_path):
    file_path = os.path.join(image_path, file)
    # 获取文件的扩展名
    file_ext = os.path.splitext(file)[1]
    # 判断是否为.jpg或.JPEG格式
    if file_ext.lower() not in [".jpg", ".jpeg"]:
        # 删除该文件
        os.remove(file_path)
        # 获取文件名的前缀部分
        file_prefix = os.path.splitext(file)[0]
        # 拼接xml文件的路径
        xml_file = os.path.join(xml_path, file_prefix + ".xml")
        # 判断xml文件是否存在，如果存在则删除
        if os.path.exists(xml_file):
            os.remove(xml_file)
