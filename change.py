# 导入必要的模块
import os
import xml.etree.ElementTree as ET

# 定义类别的列表
classes = ["container", "worker", "opendoor", "liftup", "containerForklift", "heavyForklift", "person"]
# 定义xml文件夹和yolo标签文件夹的路径
xml_path = r"F:\DataBase\dataset\Uintfog\xmls"
yolo_path = r"F:\DataBase\zjjdataset\dataval709\labels709"

# 如果yolo标签文件夹不存在，就创建一个
if not os.path.exists(yolo_path):
    os.makedirs(yolo_path)

# 遍历xml文件夹下的所有文件
for file in os.listdir(xml_path):
    # 如果文件不是xml格式，就跳过
    if not file.endswith(".xml"):
        continue
    # 获取文件名（不含扩展名）
    filename = os.path.splitext(file)[0]
    # 读取xml文件
    xml_file = os.path.join(xml_path, file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # 获取图片的宽度和高度
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    # 创建一个空列表，用于存储yolo格式的标签
    yolo_labels = []
    # 遍历xml文件中的所有目标
    for obj in root.findall("object"):
        # 获取目标的类别名称
        name = obj.find("name").text
        # 如果类别名称不在类别列表中，就跳过
        if name not in classes:
            continue
        # 获取目标的类别索引（从0开始）
        cls_id = classes.index(name)
        # 获取目标的边界框坐标（xmin, ymin, xmax, ymax）
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)
        # 计算目标的中心点坐标（x, y）和宽度和高度（w, h），并归一化到0-1之间
        x = (xmin + xmax) / 2 / width
        y = (ymin + ymax) / 2 / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height
        # 将类别索引和归一化后的坐标拼接成一个字符串，添加到yolo标签列表中
        yolo_label = f"{cls_id} {x} {y} {w} {h}"
        yolo_labels.append(yolo_label)
    # 如果yolo标签列表不为空，就将其写入对应的yolo标签文件中
    if yolo_labels:
        yolo_file = os.path.join(yolo_path, filename + ".txt")
        with open(yolo_file, "w") as f:
            for label in yolo_labels:
                f.write(label + "\n")
