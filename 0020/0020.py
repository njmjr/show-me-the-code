# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 15:38:44 2015

@author: zhangbohun
"""

import xlrd

def phone_calls(xls_file):
    xls = xlrd.open_workbook(xls_file)
    sheet = xls.sheet_by_index(0)
    seconds = 0
    minutes =0
    for i in range(1, sheet.nrows):
        seconds += int(sheet.row_values(i)[3])
    minutes += seconds / 60
    seconds = seconds % 60
    print '通话时长：', minutes, '分', seconds, '秒'

if __name__ == '__main__':
    phone_calls('example.xls')
    