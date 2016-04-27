#!/usr/bin/env python
# encoding: utf-8
import urlfunc
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

def crawler()
list_all = getlist()
for a,b in list_all.items():
    print a,b
