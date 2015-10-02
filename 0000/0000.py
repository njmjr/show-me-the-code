# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 19:46:32 2015

@author: zhangbohun
"""
from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, num):
    img = Image.open(picPath)
    width, height = img.size
    fillcolor = '#ff0000'#'red',(255,0,0)
    myfont = ImageFont.truetype('Arial.ttf', width / 3)
    ImageDraw.Draw(img).text((4 * width / 5, 0), str(num), font = myfont, fill = fillcolor)
    img.save('new_picture.jpg')
    #img.show()

if __name__ == '__main__':
    add_num('picture.jpg', 1)