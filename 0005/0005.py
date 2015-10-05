# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 12:52:24 2015

@author: zhangbohun
"""

from PIL import Image
import os

def reSize(dirPath, ResizeX = 100, ResizeY = 100):
    picturelist=os.listdir(dirPath)
    for picture in picturelist:
        #print picture
        img = Image.open(dirPath+picture)
        x,y=img.size
        if x<ResizeX:
            tmp_X=x
        else:
            tmp_X=ResizeX
        if y<ResizeY:
            tmp_Y=y  
        else:
            tmp_Y=ResizeY
        new = img.resize((tmp_X, tmp_Y))
        new.save(picture.split('.')[0] + '_modifid' + '.png')

if __name__ == '__main__':
    reSize('img/',  640,1136)