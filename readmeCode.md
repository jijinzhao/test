1.add.py 为图片重命名，以数字的递增的方式

2.change.py将xml标签格式转换为yolo标签格式

3.adjust.py将有标签的图片保存下来，没有标签的图片文件删掉

代码逻辑（使用python生成代码，要求：读取C:\Users\Administrator\Desktop\test\images下的所有文件如果文件是图片将文件名记录在imageUint.txt中如果不是图片跳过该文件，读取C:\Users\Administrator\Desktop\test\xml下的所有文件如果文件格式是xml将文件名记录在xmlUint.txt中，记录好两个文件夹的名字后，在xmlUint.txt中名字存在的对应名字的图片可以在C:\Users\Administrator\Desktop\test\images下保存下来，如果C:\Users\Administrator\Desktop\test\images中存在xmlUint.txt中没有对应名字的图片则要删除该图片 ）[实际代码为newbing优化后十分强大]

4.jpg.py只保留jpg图片文件

（使用python生成代码，要求：现在有文件夹F:\DataBase\dataset\Uint\imagesUint和文件夹F:\DataBase\dataset\Uint\xmlUint，遍历F:\DataBase\dataset\Uint\imagesUint所有文件如果文件的格式是.jpg或.JPEG则跳过如果不是则删除该文件，同时删除在F:\DataBase\dataset\Uint\xmlUint文件夹下相同名称的文件 ）

5.ordername.py 使得图片和标签相对应的前提下，为图片和标签重命名

（使用python生成代码，要求：访问文件夹C:\Users\Administrator\Desktop\test\images下所有的文件，将文件按名字中的数字从小到大排序，然后对所有文件重命名，最小名字的文件命名为1，每次加1，依次递增；访问文件夹C:\Users\Administrator\Desktop\test\xml下所有的文件，将文件按名字中的数字从小到大排序，然后对所有文件重命名，最小名字的文件命名为1，每次加1，依次递增 ）

6.Dcdhe.py对一个文件夹内的所有文件进行去雾算法处理，去完雾的图片放在另一个文件夹内

7.spilt.py划分图片和标签文件夹成训练集和测试集