#encoding:utf8
import requests
from bs4 import BeautifulSoup
import time


def get_150():
    print('开始捉数据！')
    THE_URL = 'http://bbs.jrj.com.cn/tag_126'
    for page in range(1,141):
        HEADERS = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        time.sleep(5)
        try:
            URL = THE_URL
            print(URL)
            session1 = requests.session()
            response1 = session1.get(URL,headers = HEADERS)
            html_source_code = response1.content
            # print(html_source_code.content)
            soup = BeautifulSoup(html_source_code,'lxml')
            soup = soup.find('div',class_='htags mgtf20')
            # print(soup)
            # time.sleep(10)
            for tags in soup.find_all('li'):
                print(tags.text)
            # print(soup)
            # print(URL)
        except Exception as e:
            continue


get_150()

















