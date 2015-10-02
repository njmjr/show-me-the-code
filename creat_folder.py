# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 20:14:56 2015

@author: zhangbohun
"""
import os
# 创建文件夹 0000～0025
for i in range(26):
    n = str(i).zfill(4)
    sub_path = n
    os.mkdir(sub_path)