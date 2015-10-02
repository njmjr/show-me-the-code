# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 21:05:06 2015

@author: zhangbohun
"""
import uuid

def generate_activation_code(count):
    code_list = []
    for i in xrange(count):
        code = str(uuid.uuid4()).upper()
        if code not in code_list:#唯一性是关键，这里用uuid基本不会有重复的可能
        #但是如果使用随机数实现的话就不一定了，除了用not in来解决以外，也可以用set()来存储结果，然后判断是否够200个
            code_list.append(code)
    return code_list

if __name__ == "__main__":
    code_list = generate_activation_code(200)
    for code in code_list:
        print code
    #可以转换为字典看keys 是否是200判断是否有重，不过只能作为确认
    #print(len({}.fromkeys(code_list).keys()))