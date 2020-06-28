# 批量席位卡生成工具
==================

batch banquet-card generator

用于批量生成席位卡，席位卡卡面大小为200mm x 100mm

## 环境

Python 3.x   
Pillow库  

### 环境准备

1. 安装 Python 3.x
2. 安装依赖库
```
pip install Pillow
```
3. 准备字体文件（ttf）

## 如何使用

1. 下载source文件夹
2. 将字体文件放到source文件夹内，命名为```fz.ttf``` ，参见```generate.py```第24行
3. 按照 ```o.data.png```的样式，编辑背景后，保存为 ```o.data```
4. 编辑names.txt文件，每行一个姓名
5. 运行 ```generate.py``` 以批量生成相关图片文件

## 文件说明

1. ```o.data```是PNG格式的背景文件
2. ```names.txt``` 是UTF-8编码的姓名清单
3. ```fz.ttf``` 是字体文件，本库未提供，请自行下载，依授权使用
4. ```export```文件夹，存放生成的图片
