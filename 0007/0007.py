# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 14:19:40 2015

@author: zhangbohun
"""

import os

def count_codelines(dirPath):#返回字典
    code_filelist=os.listdir(dirPath)
    code_lines = 0
    empty_lines = 0
    comment_lines = 0
    for code_file in code_filelist:
        with open(dirPath+code_file,'rb')as f:
            codes_lines = f.readlines()
        for codes_line in codes_lines:
            codes_line = codes_line.strip()
            if codes_line.startswith('#'):#这里是没有考虑多行注释的
                comment_lines += 1
            elif codes_line == "":
                empty_lines += 1
            else:
                code_lines += 1
    print('code lines: ' + str(code_lines))
    print('comment lines: ' + str(comment_lines))
    print('empty lines: ' + str(empty_lines))

if __name__ == '__main__':
    count_codelines('codes/')