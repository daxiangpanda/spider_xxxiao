#!/usr/bin/env python
# encoding: utf-8
import urlfunc
import os
import urllib2
from bs4 import BeautifulSoup
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
    if not os.path.isdir(area):
        os.mkdir(area)
    page = 0
    while True:
        url_area = url+'/page/'+str(page)
        # print url_area
        try:
            soup = urlfunc.url_open(url_area)
        except urllib2.URLError:
            print 'complete'
            break
        print url_area
        page+=1


list_all = getlist()
crawler('abc',list_all.values()[1])
# for a,b in list_all.items():
    # print a,b
