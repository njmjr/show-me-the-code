# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 13:38:26 2015

@author: zhangbohun
"""

import json
import xlwt

def txt_to_xls(txt_file):
    with open(txt_file,'r') as f:
        json_content = json.load(f)
    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workbook.add_sheet('city', cell_overwrite_ok=True)
    
    for i in range(len(json_content)):
        # 写入对应行列
        row = i
        col = 0
        
        #顺序不对
        #sheet.write(row, col, json_content.keys()[i])
        #json_data = json_content[json_content.keys()[i]]
        
        #不过这里碰巧可以用数字做key
        sheet.write(row, col, i+1)
        json_data = json_content[str(i+1)]
        sheet.write(row,col+1,json_data)
    workbook.save('city.xls')
		
if __name__ == '__main__':
	txt_to_xls('city.txt')