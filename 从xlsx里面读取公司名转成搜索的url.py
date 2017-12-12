#encoding:utf-8
#从xlsx里面读取80家公司名,然后转换成url


import xlrd
import xlwt
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib #要对汉字进行url编码,urllib.parse.quote(names)
import pandas as pd






def get_page_source(need_url):

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    )

    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.get(need_url)#http://www.tianyancha.com/company/35027356
    time.sleep(6)
    content = driver.page_source
    # print(content)
    soup = BeautifulSoup(content,'lxml')
    driver.close()
    return soup








work_book = xlrd.open_workbook('C:/Users/Administrator/Desktop/youtube的程序/PE已投项目.xlsx')
the_sheet = (work_book.sheet_by_name('海通创新已投项目'))
name_list = (the_sheet.col_values(0))
# urls_list = []
the_dict = {}
for names in name_list:
    urls_encode = urllib.parse.quote(names)
    # print(urls_encode)
    search_urls = "http://www.tianyancha.com/search?key={}&checkFrom=searchBox".format(urls_encode)
    # print(search_urls)
    soup_all = get_page_source(search_urls)
    the_soup = soup_all.find('body').find('a',class_ = "query_name search-new-color sv-search-company")
    print(names)
    print(the_soup.get('href'))
    the_dict[names] = the_soup.get('href')
    # urls_list.append(the_soup('href'))
print(the_dict)

# t_dict = {'北京爱旅伟邦科技有限公司':'http://www.tianyancha.com/company/35027356','北京聚能鼎力科技股份有限公司':'http://www.tianyancha.com/company/176277626','北京麦轮泰电子商务有限公司':'http://www.tianyancha.com/company/2350428804'}
#把一个字典转化成csv存起来,单一的数据指向：pd.Series
df = pd.Series(the_dict)
print(df)
df.to_csv('company_urls.csv')
# df = pd.DataFrame(t_dict)
# print(df)
# (df.to_csv('ddddddd.csv'))


#http://www.tianyancha.com/search?key=%E9%9D%92%E5%B2%9B%E8%BE%BE%E8%83%BD%E7%8E%AF%E4%BF%9D%E8%AE%BE%E5%A4%87%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox
#http://www.tianyancha.com/search?key=names&checkFrom=searchBox

# soup = get_page_source('http://www.tianyancha.com/search?key=%E5%8C%97%E4%BA%AC%E7%88%B1%E6%97%85%E4%BC%9F%E9%82%A6%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox')
# print(soup)















































































