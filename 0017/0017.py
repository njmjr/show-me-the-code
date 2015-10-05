# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 13:59:27 2015

@author: zhangbohun
"""

import xlrd
from xml.dom import minidom

def xls_to_xml(xls_file):
    data = xlrd.open_workbook(xls_file)
    sheet = data.sheet_by_index(0)        #通过索引获取xls文件第0个sheet
    rows = sheet.nrows
    dic = {}
    for i in range(rows):
        dic[str(i+1)] =sheet.row_values(i)[:]
    #print dic
    
    #建立Dom Object
    doc = minidom.Document()
    #建立root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    #建立'students' tag
    students = doc.createElement('students')
    root.appendChild(students)
    #增加注释comment element
    students.appendChild(doc.createComment("学生信息表\"id\" : [名字, 数学, 语文, 英文]"))
    #增加text element
    students.appendChild(doc.createTextNode(str(dic)))#这里的汉字问题无力吐槽，引号也不对。。。

    #保存
    student_xml = open('student.xml','w')
    student_xml.write(doc.toprettyxml())
    student_xml.close()
    
if __name__ == '__main__':
    xls_to_xml('student.xls')