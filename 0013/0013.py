# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 12:14:56 2015

@author: zhangbohun
"""

import urllib
#import urllib2
import os
from bs4 import BeautifulSoup

def get_images(url):
    #req = urllib.Request(url)
    #req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36')
    #soup = BeautifulSoup(urllib2.urlopen(req).read())
    soup = BeautifulSoup(urllib.urlopen(url).read())
    s_imgs = soup.find_all('img', pic_type='0')
    #print s_img
    
    if os.path.exists('pictures'):
        os.chdir('pictures')
    else:
        os.makedirs('pictures')
        os.chdir('pictures')
        
    for s_img in s_imgs:
        img_url = s_img['src']
        file_name = img_url.split('.')[-2].split('/')[-1]+'.jpg'
        urllib.urlretrieve(img_url, file_name)
    os.chdir('..')
    
if __name__ == '__main__':
    get_images(url='http://tieba.baidu.com/p/2166231880')