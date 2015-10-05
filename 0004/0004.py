# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 12:30:18 2015

@author: zhangbohun
"""

import re

def count_word(filepath):
    with open(filepath,'rb')as f:
        txt = f.read()
    words = re.findall(r'[a-zA-Z0-9]+', txt)#[a-zA-Z0-9]+或者[\w]+
#    dic = {}
#    for word in words:
#        if word is '':
#            continue
#        if word in dic:
#            dic[word] += 1
#        else:
#            dic[word] = 1
#    return dic
    return len(words)

if __name__ == '__main__':
    print count_word('English.txt')