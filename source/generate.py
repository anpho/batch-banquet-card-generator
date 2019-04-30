# -*- coding:utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

print("席位卡批量打印 1.0版")
print("====================")
print('''使用说明：
先打开姓名.txt，以每行一个姓名的方式编辑文件并保存
然后再打开这个应用，会在当前目录export目录下生成席位卡图片
''')
if not os.path.exists(".\\export") :
    os.mkdir(".\\export")

print("读取：names.txt")

# 读取姓名清单
file = open("names.txt","r",-1,"utf-8")
names = file.readlines()
file.close()

bg="./o.data"

font = ImageFont.truetype("./fz.ttf", 300)
color="#000000"

for name in names :
    bgi=Image.open(bg)
    w,h=bgi.size
    cur = name.strip()
    print("正在生成： %s" % cur)
    output_file="./export/%s.jpg" % cur
    draw = ImageDraw.Draw(bgi)
    textw,texth=draw.textsize(cur,font)
    draw.text((w/2-textw/2,945),u'%s' % cur,'#000000',font)
    draw.text((w/2-textw/2,2282),u'%s' % cur,'#000000',font)
    bgi.save(output_file,'jpeg')


os.system("explorer .\\export")

