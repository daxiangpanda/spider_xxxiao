from bs4 import BeautifulSoup
# with open('abc\\1','r') as f:
    # soup = f.read()
import os
import urlfunc
import urllib
def save(data,pic_name,path_webpage):
    # print path_webpage+pic_name
    # print path_webpage
    with open(path_webpage+'/'+pic_name,'w') as f:
        f.write(data)
def process_1(soup):
    res = {}
    for i in soup.find_all('h2',class_='entry-title'):
        res[i.find('a').string]=i.find('a')['href']
    print res
    for a,b in res.items():
        print a,b
    return res

def process_2(path_webpage,url):
    if not os.path.isdir(path_webpage):
        os.mkdir(path_webpage)
    soup = urlfunc.url_open(url)
    for i in soup.find_all('a',rel='rgg'):
        pic_name = i['href'].split('_')[-1]
        pic_data = urllib.urlopen(i['href']).read()
        print pic_name
        # print pic_data
        save(pic_data,pic_name,path_webpage)
