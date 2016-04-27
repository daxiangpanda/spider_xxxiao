#!/usr/bin/env python
# encoding: utf-8
import urlfunc
import os
import urllib2
from bs4 import BeautifulSoup
import process_soup
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
        url_area = url+'page/'+str(page)
        print url_area
        try:
            soup = urlfunc.url_open(url_area)
            print area
            print url_area
            path_area = os.path.join(area,url_area.split('/')[-1])
            print path_area

            webpage_info = process_soup.process_1(soup)
            for name,url in webpage_info.items():
                path_webpage = os.path.join(path_area, name)
                process_soup.process_2(path_webpage,url)
        except urllib2.URLError:
            print 'complete'
            break
        print url_area
        page+=1


list_all = getlist()
for i in range(len(list_all)):
    crawler(list_all.keys()[i],list_all.values()[i])

