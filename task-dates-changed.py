# -*- coding:UTF-8 -*-
import urllib2
import numpy as np
import MySQLdb
import time
import math
import xlrd
import pandas as pd

def Token():                    ###定义令牌函数
    req = urllib2.Request('http://v2.yundzh.com/token/access?appid=dcdc435cc4aa11e587bf0242ac1101de&secret_key=InsQbm2rXG5z')
    f = urllib2.urlopen(req)
    f=f.read()
    f=eval(f)
    f=f['Data']['RepDataToken'][0]['token']
    return f
def timetran(t):
	timeStamp = t
	timeArray = time.localtime(timeStamp)
	t = time.strftime("%Y-%m-%d", timeArray)
	return t

def qushuju(stockcode,begin_time,mubiaojia):
	for zhixingcishu in range(10):
		try:
			url='http://gw.yundzh.com/quote/kline?obj=%s&begin_time=%s-000000-000-0&field=ShiJian,ShouPanJia,ZuiGaoJia,ZuiDiJia&split=1&period=1day&token=%s'%(stockcode,begin_time,Token())
			req = urllib2.Request(url)
			f = urllib2.urlopen(req)
			f=f.read()
			f=eval(f)
			f=f['Data']['JsonTbl']['data'][0][0]['data'][0][1]['data']
			break
		except Exception,e:
			if zhixingcishu==9:
				print e
				print 'error'
			else:
				continue
	data=[[timetran(x[0]),x[1],x[2],x[3]] for x in f]
	data=data[:25]
	return chuli(data,mubiaojia)

def chuli(data,mubiaojia):
	shifouzhisun=''
	shixian=''
	tuijianrijiage=data[0][3]
	jiezhiriqi=data[-1][0]
	jiezhirijiage=data[-1][3]
	mubiaojia_1=round((mubiaojia-tuijianrijiage)*1+tuijianrijiage,2) ####################比例r
	zhisunjia=0.5*tuijianrijiage                                  ####################################止损价
	for i,value in enumerate(data):
		if value[2]<zhisunjia:
			zhisunriqi=value[0]
			break
	else:
		zhisunriqi='none'
	for i,value in enumerate(data):
		if value[1]>mubiaojia_1:
			mubiaoriqi=value[0]
			break
	else:
		mubiaoriqi='none'
	data.sort(key=lambda x:x[2])
	zuidijia=data[0][2]
	zuidijiari=data[0][0]
	data.sort(key=lambda x:x[1])
	zuigaojia=data[-1][1]
	zuigaojiari=data[-1][0]
	return tuijianrijiage,mubiaojia,mubiaojia_1,zhisunjia,jiezhiriqi,jiezhirijiage,mubiaoriqi,zhisunriqi,shifouzhisun,shixian,zuigaojia,zuigaojiari,zuidijia,zuidijiari

filename='test.xlsx'
wk=xlrd.open_workbook(filename)
sh=wk.sheets()[0]
stocks=sh.col_values(1)
date=sh.col_values(0)
date=[str(x)[:-2] for x in date]
mubiaojia=sh.col_values(2)
result=map(qushuju,stocks,date,mubiaojia)
result=pd.DataFrame(result)
result.columns =['买入价','目标价','比例目标价','止损价','截止日','截止价格','到达目标价格日期','止损日期','null','null','最高价','最高价日期','最低价','最低价日期']
result.to_excel('result.xlsx')
