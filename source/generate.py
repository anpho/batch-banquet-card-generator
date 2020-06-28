# -*- coding:utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

print("席位卡批量打印 1.1版")
print("====================")
print('''使用说明：
先打开姓名.txt，以每行一个姓名的方式编辑文件并保存
然后再打开这个应用，会在当前目录export目录下生成席位卡图片
''')
if not os.path.exists(".\\export"):
    os.mkdir(".\\export")

print("读取：names.txt")

# 读取姓名清单
file = open("names.txt", "r", -1, "cp936")
names = file.readlines()
file.close()

# 背景图片
bg = "./o.data"

font = ImageFont.truetype("./fz.ttf", 325)
color = "#000000"

for name in names:
    bgi = Image.open(bg)
    w, h = bgi.size
    cur = name.strip()
    if (len(cur) == 0):
        continue
    print("正在生成： %s" % cur)
    output_file = "./export/%s.jpg" % cur

    draw = ImageDraw.Draw(bgi)
    textw, texth = draw.textsize(cur, font)

    # 旋转180度
    image_upside_down = Image.new('RGBA', (textw, texth))
    draw_upside_down = ImageDraw.Draw(image_upside_down)
    draw_upside_down.text((0, 0), u'%s' % cur, color, font)
    image_upside_down = image_upside_down.rotate(
        180, expand=0, fillcolor='white')

    draw.text((w/2-textw/2, 1650), u'%s' % cur, color, font)
    bgi.paste(image_upside_down, (int(w/2-textw/2), 500), image_upside_down)

    # 保存
    bgi.save(output_file, 'jpeg')


os.system("explorer .\\export")
