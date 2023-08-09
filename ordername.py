# 导入os和re模块
import os
import re

# 定义图片和xml文件的路径
image_path = r"F:\DataBase\dataset\Uint709\imagesUint2"
xml_path = r"F:\DataBase\dataset\Uint709\xmlUint2"

# 定义一个函数，用于提取文件名中的数字
def get_number(filename):
    # 使用正则表达式匹配数字
    match = re.search(r"\d+", filename)
    # 如果匹配成功，则返回数字，否则返回0
    if match:
        return int(match.group())
    else:
        return 0

# 定义一个函数，用于重命名文件夹下的所有文件
def rename_files(folder_path):
    # 获取文件夹下的所有文件
    files = os.listdir(folder_path)
    # 按照文件名中的数字从小到大排序
    files.sort(key=get_number)
    # 初始化新的文件名为1
    new_name = 1
    # 遍历所有文件
    for file in files:
        # 获取文件的扩展名
        file_ext = os.path.splitext(file)[1]
        # 拼接原始文件的路径
        old_file = os.path.join(folder_path, file)
        # 拼接新的文件的路径，使用新的文件名和原始扩展名
        new_file = os.path.join(folder_path, str(new_name)+ file_ext)
        # 重命名文件
        os.rename(old_file, new_file)
        # 新的文件名加1
        new_name += 1

# 调用函数，分别重命名图片和xml文件夹下的所有文件
rename_files(image_path)
rename_files(xml_path)
