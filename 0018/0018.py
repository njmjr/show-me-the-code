# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 15:03:05 2015

@author: zhangbohun
"""

import xlrd,json
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
    #建立'city' tag
    students = doc.createElement('city')
    root.appendChild(students)
    #增加注释comment element
    students.appendChild(doc.createComment("城市信息"))
    #增加text element
    j = json.dumps(dic, ensure_ascii=False, indent=6)
    #汉字用json弄好了，又多了个引号问题（双引号变&quot;）。。。暂时用单引号
    students.appendChild(doc.createTextNode(j.decode('utf-8').replace('\"','\'')))
    
    #保存
    student_xml = open('city.xml','w')
    student_xml.write(doc.toprettyxml())
    student_xml.close()
    
if __name__ == '__main__':
    xls_to_xml('city.xls')