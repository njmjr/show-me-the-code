# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 15:26:45 2015

@author: zhangbohun
"""

import urllib
from bs4 import BeautifulSoup

def show_href(url):
    content = urllib.urlopen(url).read()
    soup = BeautifulSoup(content)
    for tag in soup.find_all('a'):
        try:
            if tag['href'].startswith('http'):
                print tag['href']
        except KeyError:
            pass

if __name__ == '__main__':
    show_href('http://zhangbohun.github.io/2015/08/05/%E4%BA%BA%E7%94%9F%E6%B8%B8%E6%88%8F/')