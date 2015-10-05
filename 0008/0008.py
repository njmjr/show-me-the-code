# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 14:56:25 2015

@author: zhangbohun
"""

import urllib2
from bs4 import BeautifulSoup

def show_content(url, content_tag, content_tag_class):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    for tag in soup.find_all(content_tag, content_tag_class):
        print tag.text

if __name__ == '__main__':
    show_content('http://zhangbohun.github.io/2015/08/05/%E4%BA%BA%E7%94%9F%E6%B8%B8%E6%88%8F/', 'div', 'article-content')