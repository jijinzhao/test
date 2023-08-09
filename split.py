# 导入所需的库
import os
import random
import shutil

# 定义图片和标签的源文件夹和目标文件夹
img_src = "F:\\DataBase\\dataset\\Uintfog\\imagespro"
label_src = "F:\\DataBase\\dataset\\Uintfog\\yolopro"
img_train = "F:\\DataBase\\dataset\\Uintfog\\train\\images"
img_test = "F:\\DataBase\\dataset\\Uintfog\\test\\images"
label_train = "F:\\DataBase\\dataset\\Uintfog\\train\\labels"
label_test = "F:\\DataBase\\dataset\\Uintfog\\test\\labels"

# 定义划分比例，例如0.8表示80%的数据用于训练，20%的数据用于测试
split_ratio = 0.8

# 获取图片和标签的文件名列表
img_list = os.listdir(img_src)
label_list = os.listdir(label_src)

# 打乱图片和标签的顺序
random.shuffle(img_list)
random.shuffle(label_list)

# 计算训练数据和测试数据的数量
train_num = int(len(img_list) * split_ratio)
test_num = len(img_list) - train_num

# 检测目标文件夹是否存在，如果不存在则创建
if not os.path.exists(img_train):
    os.makedirs(img_train)
if not os.path.exists(img_test):
    os.makedirs(img_test)
if not os.path.exists(label_train):
    os.makedirs(label_train)
if not os.path.exists(label_test):
    os.makedirs(label_test)

# 将图片和标签复制到对应的目标文件夹
for i in range(train_num):
    img_name = img_list[i]
    label_name = img_name.split(".")[0] + ".txt"
    shutil.copy(os.path.join(img_src, img_name), os.path.join(img_train, img_name))
    shutil.copy(os.path.join(label_src, label_name), os.path.join(label_train, label_name))

for i in range(train_num, len(img_list)):
    img_name = img_list[i]
    label_name = img_name.split(".")[0] + ".txt"
    shutil.copy(os.path.join(img_src, img_name), os.path.join(img_test, img_name))
    shutil.copy(os.path.join(label_src, label_name), os.path.join(label_test, label_name))

# 打印划分结果
print("划分完成，训练数据集有{}张图片和标签，测试数据集有{}张图片和标签。".format(train_num, test_num))
