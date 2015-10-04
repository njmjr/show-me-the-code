# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 16:32:33 2015

@author: zhangbohun
"""

def filter(testWord):
    with open('filtered_words.txt','rb')as f:
        filtered_words=[line.replace('\r\n','') for line in f]
        #print filtered_words
    for filtered_word in filtered_words:
        if filtered_word in testWord.encode('gbk'):#包含敏感词
            print 'Freedom'
            break#return
    else:
        print 'Human Rights'

if __name__ == '__main__':
    filter(u'c北京ssloves')