# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:23:48 2017

@author: Administrator
"""

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup as bs
import time
#import sys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'https://www.tianyancha.com/')
driver.find_element_by_class_name("media_port").click()
time.sleep(1)
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[2]/div/div[2]/div[2]/div[1]/div[1]').click()
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[2]/div/div[2]/div[2]/div[2]/div[2]/input').clear()
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[2]/div/div[2]/div[2]/div[2]/div[2]/input').send_keys('18502285299')
time.sleep(1)
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[2]/div/div[2]/div[2]/div[2]/div[3]/input').clear()
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[2]/div/div[2]/div[2]/div[2]/div[3]/input').send_keys('fxj19960614')
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[2]/div/div[2]/div[2]/div[2]/div[5]').click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='live-search']").clear()
driver.find_element_by_xpath(".//*[@id='live-search']").send_keys('杭州立方控股股份有限公司')
driver.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/\
                             div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div').click()
time.sleep(2)
driver.find_element_by_xpath('html/body/div[2]/div[1]/div/div/\
                             div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/a/span/em').click()
time.sleep(1)
windows = driver.window_handles
driver.switch_to_window(windows[1])
time.sleep(0.5)

page = bs(driver.page_source)
#print(page.contents)
'''
the_soup = page.find('div',attrs ={'id':'_container_seniorPeople'})
the_soup_1 = the_soup.find('tbody')
the_soup_2 = the_soup_1.find_all('span')
data_list = [ele.get('onclick') for ele in the_soup_2]
for i in data_list:
    i = 0
    data_list_1 = data_list[i][16:]
    data_dic = eval(data_list_1)
    print(data_dic)
    i += 1
'''
time.sleep(0.5)
info = driver.find_element_by_xpath(".//*[@id='_container_seniorPeople']/div/div/ul/li[4]/a")
info1 = driver.find_element_by_xpath(".//*[@id='nav-main-holdingCompanyNum']")
time.sleep(0.5)
actions = ActionChains(driver)
actions.move_to_element(info1)
actions.perform()
time.sleep(5)
info.click()
time.sleep(10)
page_1 = bs(driver.page_source)
the_soup_3 = page_1.find('div',attrs ={'id':'_container_seniorPeople'})
the_soup_4 = the_soup_3.find('tbody')
the_soup_5 = the_soup_4.find_all('span')
data_list_1= [ele1.get('onclick') for ele1 in the_soup_5]
for s in data_list_1:
    s = 0
    data_list_2 = data_list_1[s][16:]
    data_dic_1= eval(data_list_2)
    print(data_dic_1)
    s += 1
