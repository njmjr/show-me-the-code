# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 21:51:38 2015

@author: zhangbohun
"""
import uuid
import MySQLdb

def generate_activation_code(count):
    code_list = []
    for i in xrange(count):
        code = str(uuid.uuid4()).upper()
        if code not in code_list:
            code_list.append(code)
    return code_list
    
def store_mysql(code_list):
    conn = MySQLdb.connect("localhost",user = 'root', password = 'password', database = 'testDB')
    cursor = conn.cursor()

    #已经存在则删除
    cursor.execute("drop table if exists code_table")
    cursor.execute('CREATE TABLE code_table (code_value char(40) not null);')
    for code in code_list:
        cursor.execute('insert into code_table (code_value) values("%s")' % (code))
        
    conn.commit()
    #conn.rollback()
    cursor.close()
    conn.close()
    
if __name__ == '__main__':
    store_mysql(generate_activation_code(200))