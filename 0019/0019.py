# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 15:25:05 2015

@author: zhangbohun
"""

import xlrd
from xml.dom import minidom

def xls_to_xml(xls_file):
    data = xlrd.open_workbook(xls_file)
    sheet = data.sheet_by_index(0)        #通过索引获取xls文件第0个sheet
    rows = sheet.nrows
    list = []
    for i in range(rows):
        list.append(sheet.row_values(i)[:])
    #print list
    
    #建立Dom Object
    doc = minidom.Document()
    #建立root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    #建立'numbers' tag
    students = doc.createElement('numbers')
    root.appendChild(students)
    #增加注释comment element
    students.appendChild(doc.createComment("数字信息"))
    #增加text element
    students.appendChild(doc.createTextNode(str(list)))

    #保存
    student_xml = open('numbers.xml','w')
    student_xml.write(doc.toprettyxml())
    student_xml.close()
    
if __name__ == '__main__':
    xls_to_xml('numbers.xls')