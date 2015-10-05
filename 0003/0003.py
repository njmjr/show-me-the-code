# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 20:06:16 2015

@author: zhangbohun
"""

import uuid
import redis

def generate_activation_code(count):
    code_list = []
    for i in xrange(count):
        code = str(uuid.uuid4()).upper()
        if code not in code_list:
            code_list.append(code)
    return code_list

def store_redis(code_list):
    r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
    for code in code_list:
        r.lpush('code', code)
    r.save()
    
if __name__ == '__main__':
    store_redis(generate_activation_code(200))



