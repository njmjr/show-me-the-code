# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 15:56:50 2015

@author: zhangbohun
"""

import os
from hashlib import sha256
from hmac import HMAC

SALT_LENGTH = 8

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(SALT_LENGTH)
    if isinstance(password, unicode):
        password = password.encode('UTF-8')
    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()
    return salt + result

def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:SALT_LENGTH])#前八位是盐

if __name__ =='__main__':
    password = 'secret_password'
    encrypt = encrypt_password(password)
    print validate_password(encrypt, password)