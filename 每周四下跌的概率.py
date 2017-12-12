# -*- coding:UTF-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime




def dateRange(start, end):# 定义一个函数叫做dateRange，在给定两个日期之后，取出这两个日期的之间的所有日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1 #datetime.datetime.strptime(date_string, format),将格式字符串转换为datetime对象,现在是计算出了两个日期之间的天数
    return [datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(i), "%Y-%m-%d") for i in xrange(days)] #strftime:把一个datetime对象转成字符串格式


def zhangfu_Thursday(start_day,end_day):#定义一个函数，名字叫zhangfu
	SZ_pchange = ts.get_h_data('000001', start = start_day, end = end_day,index = True).sort_index()['close'].pct_change()#取上证50,这是一个DataFrame结构
	thur = []
	for day in dateRange('2010-05-01','2016-12-22'):
		day_date = datetime.datetime.strptime(day,'%Y-%m-%d')
		xingqi = day_date.weekday()
		if xingqi == 3:
			thur.append(day)
	all_list = []
	for thursday in thur:
		
		try:
			all_list.append(SZ_pchange[thursday])
		except:
			continue
	down_number = len(filter(lambda x:x < 0, all_list))
	print float(down_number)/(len(all_list))
start_end_day = ['2010-05-01','2016-12-22']
data=zhangfu_Thursday(start_end_day[0],start_end_day[1])



















