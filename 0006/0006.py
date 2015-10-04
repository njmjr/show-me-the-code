# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 14:07:03 2015

@author: zhangbohun
"""
import re
import os

def count_word(dirPath):#返回字典
    diarieslist=os.listdir(dirPath)
    dic = {}
    for diary in diarieslist:
        with open(dirPath+diary,'rb')as f:
            txt = f.read()
        words = re.findall(r'[a-zA-Z0-9]+', txt)#[a-zA-Z0-9]+或者[\w]+
        for word in words:
            if word is '':
                continue
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    dic= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)#字典排序
    return dic

if __name__ == '__main__':
    for word in count_word('diaries/'):
       print word[0]+': '+str(word[1])