# -*- coding:UTF-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
def dateRange(start, end):# 定义一个函数叫做dateRange，在给定两个日期之后，取出这两个日期的之间的所有日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1 #datetime.datetime.strptime(date_string, format),将格式字符串转换为datetime对象,现在是计算出了两个日期之间的天数
    return [datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(i), "%Y-%m-%d") for i in xrange(days)] #strftime:把一个datetime对象转成字符串格式
###先返回出两个日期之间的天数
###strftime把datetime格式变成str格式，即最后会打印出一个字符串。
###但是函数传入的是一个字符串，所以要先用strptime格式来转成一个datetime格式


def zhangfu(start_day,end_day):#定义一个函数，名字叫zhangfu
	SZ50 = ts.get_h_data('000016',index = True,start = start_day,end = end_day)[['close']]#取上证50,这是一个DataFrame结构
	SZ50.columns = ['上证50'] #设置列名
	data0 = SZ50 #现在data0就是上证50指数
	data0 = data0[::-1]# 倒序排列
	mon = []
	fri = []
	for day in dateRange('2004-05-31','2016-11-25'):
		day_date=datetime.datetime.strptime(day,'%Y-%m-%d')
		xingqi=day_date.weekday()
		if xingqi==0:
			mon.append(day)
		if xingqi==4:
			fri.append(day)
	data0['index']=data0.index
	percentage_list = []
	winnings_list = []
	for couple in zip(mon,fri):
		try:
			mon_price=data0.loc[couple[0],'上证50']
			fri_price=data0.loc[couple[1],'上证50']
			percentage = (fri_price - mon_price)/mon_price
			if -0.2 < percentage < 0.2:
				percentage_list.append(percentage)
				winnings = 0.05*(100/0.1019) - (100/0.1019)*0.005
				winnings_list.append(winnings)

			#percentage_list.append(percentage)
			#percentage = (len(filter(lambda x:  x >= 0.1 ,percentage_list)))/float(len(percentage_list))#后面加一个float因为要做真正的除法
		except Exception as e:
			#print(e)
			continue
	print len(percentage_list)
	print len(zip(mon,fri))
	print sum(winnings_list)
	print len(winnings_list)
	print sum(winnings_list)/len(winnings_list)
	return data0


qizhiriqi=['2004-05-31','2016-11-25']
data=zhangfu(qizhiriqi[0],qizhiriqi[1])
# print data
# data.to_excel('result.xlsx')