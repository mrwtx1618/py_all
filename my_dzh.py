# -*- coding:UTF-8 -*-
import urllib2
import numpy as np
import os
import MySQLdb
import time
import math
import xlrd
import pandas as pd
def Token():                      ###定义令牌函数，得到了令牌
    req = urllib2.Request('http://gw.yundzh.com/token/access?appid=dcdc435cc4aa11e587bf0242ac1101de&secret_key=InsQbm2rXG5z')
    f = urllib2.urlopen(req)      #f是一个instance类型
    f = f.read()                  #read之后f是一个字符串类型，f的内容为{"Qid":"","Err":0,"Counter":1,"Data":{"Id":44,"RepDataToken":[{"result":0,"token":"00000010:1480559095:88817ee13f3d9733c9eed2cd80b7df82e5434f02","create_time":1480472695,"duration":86400,"appid":"dcdc435cc4aa11e587bf0242ac1101de"}]}}
    f = eval(f)                   #eval函数将字符串类型转换成了字典类型，可以用在线json格式解析出需要的内容，现在需要的是token
    f = f['Data']['RepDataToken'][0]['token']      #取到了token
    print f
    return f                      #返回了token
Token()
# def Timetran(t):                  #定义了时间转换函数
# 	timeStamp = t
# 	timeArray = time.localtime(timeStamp)
# 	t = time.strftime("%Y-%m-%d",timeArray)
# 	return t
# def Take_data(index_code,begin_time):
# 	for execute_time in range(10):
# 		try:
# 			url = 'http://gw.yundzh.com/quote/kline?obj=%s&begin_time=%s-000000-000-0&field=ShouPanJia&split=1&period=1day&token=%s'%(index_code,begin_time,Token())

