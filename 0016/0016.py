# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 13:44:09 2015

@author: zhangbohun
"""

import json
import xlwt

def txt_to_xls(txt_file):
    with open(txt_file,'r') as f:
        json_content = json.load(f)
    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workbook.add_sheet('numbers', cell_overwrite_ok=True)
    
    for i in range(len(json_content)):#是个list
        # 写入对应行列
        row = i
        json_data = json_content[i]
        for j in range(len(json_data)):
            col=j
            sheet.write(row,col,json_data[j])
    workbook.save('numbers.xls')
		
if __name__ == '__main__':
	txt_to_xls('numbers.txt')