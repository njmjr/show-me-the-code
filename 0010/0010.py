# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 15:44:24 2015

@author: zhangbohun
"""

import random
from PIL import Image, ImageFont, ImageDraw

def create_pic():
    letters = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for x in range(4))
    im = Image.new('RGB', (120,50), (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
    draw = ImageDraw.Draw(im)
    for x in range(0,120,3):
        for y in range(0,50,3):
            im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    for i in range(4):
        font = ImageFont.truetype('arial.ttf', random.randint(20,30))
        xy = (random.randrange(0, 120), random.randrange(0, 50),
              random.randrange(0, 120), random.randrange(0, 50))
        draw.line(xy, fill=(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), width=1)
        draw.text((10+i*random.randint(25,30), random.randint(5,20)), letters[i], (random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)), font)
    im.save('result.png')

if __name__ == '__main__':
    create_pic()