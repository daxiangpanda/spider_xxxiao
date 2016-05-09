#!/usr/bin/env python
# encoding: utf-8
import urlfunc
import os
import urllib2
from bs4 import BeautifulSoup
import process_soup

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http://m.xxxiao.com/'
def getlist():
    html = urlfunc.url_open(url)
    soup = html
    result = {}
    for i in soup.find_all('nav',id="site-navigation")[0].find_all('a'):
        link = i['href']
        area = i.string.encode('utf-8')
        result[area] = link
    return result

def crawler(area,url):

    # print area
    if not os.path.isdir(area):
        os.mkdir(area)
    page = 0
    while True:
        url_area = url+'/page/'+str(page)
        print url_area

        try:
            soup = urlfunc.url_open(url_area)
            print 'area '+area
            print 'url_area '+url_area
            path_area = area+'/'+url_area.split('/')[-1]
            print dir(path_area)
            print type(path_area)
            print 'path_area '+path_area
            if not os.path.isdir(path_area):
                os.mkdir(path_area)
            webpage_info = process_soup.process_1(soup)
            if not len(webpage_info):
                break
            for name,url in webpage_info.items():
                path_webpage = os.path.join(path_area, name)
                process_soup.process_2(path_webpage,url)
        except urllib2.URLError:
            print 'complete'
            break
        print url_area
        page+=1


list_all = getlist()
for a,b in list_all.items():
    crawler(a,b)
