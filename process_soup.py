from bs4 import BeautifulSoup
# with open('abc\\1','r') as f:
    # soup = f.read()
import os
import urlfunc
import urllib
def save(data,pic_name,path_webpage):
    with open(os.path.join(path_webpage,pic_name)) as f:
        f.write(data)
def process_1(soup):
    res = {}
    for i in soup.find_all('h2',class_='entry-title'):
        res[i.find('a').string]=i.find('a')['href']
    print res
    return res

def process_2(path_webpage,url):
    if not os.path.isdir(path_webpage):
        os.mkdir(path_webpage)
    soup = urlfunc.url_open(url)
    for i in soup.find_all('a',rel='rgg'):
        pic_name = i['href'].split('_')[-1]
        pic_data = urllib.urlopen(i['href']).read()
        save(pic_data,pic_name,path_webpage)
