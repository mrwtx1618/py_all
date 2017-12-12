# -*- coding:UTF-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def zhangfu(start_day,end_day):#定义一个函数，名字叫zhangfu
	HS300 = ts.get_h_data('000300',index = True,start = start_day,end = end_day)[['close']]#取沪深300
	HS300.columns=['沪深300']
	ZZ500 = ts.get_h_data('399005',index = True,start = start_day,end = end_day)[['close']]#取中小板指
	ZZ500.columns = ['中小板指']
	SZ50 = ts.get_h_data('000016',index = True,start = start_day,end = end_day)[['close']]#取上证50
	SZ50.columns = ['上证50'] #设置列名
	SZZS = ts.get_h_data('000001',index=True,start=start_day,end=end_day)[['close']]#取上证指数
	SZZS.columns = ['上证指数']
	SZSE = ts.get_h_data('399001',index=True,start=start_day,end=end_day)[['close']]#取深证成指
	SZSE.columns = ['深证成指']
	CYBZ = ts.get_h_data('399006',index=True,start=start_day,end=end_day)[['close']]#取创业板指
	CYBZ.columns = ['创业板指']
	data0 = pd.merge(HS300,ZZ500,how = 'inner',left_index=True, right_index=True)
	data0 = pd.merge(data0, SZ50, how ='inner', left_index=True, right_index=True)
	data0 = pd.merge(data0, SZZS, how ='inner', left_index=True, right_index=True)
	data0 = pd.merge(data0, SZSE, how ='inner', left_index=True, right_index=True)
	data0 = pd.merge(data0, CYBZ, how ='inner', left_index=True, right_index=True)
	data0['date'] = data0.index
	data0 = data0.iloc[::-1]
	data0['沪深300涨幅'] = data0['沪深300'].pct_change()
	data0['中小板指涨幅'] = data0['中小板指'].pct_change()
	data0['上证50涨幅'] = data0['上证50'].pct_change()
	data0['上证指数涨幅'] = data0['上证指数'].pct_change()
	data0['深证成指涨幅'] = data0['深证成指'].pct_change()
	data0['创业板指涨幅'] = data0['创业板指'].pct_change()
	percentage = (len(filter(lambda x:  x<-0.03  ,data0['中小板指涨幅'])))/float(len(data0['中小板指涨幅']))#后面加一个float因为要做真正的除法
	print len(data0['上证指数涨幅'])
	print percentage
	data0.index = range(len(data0))
	return data0

qizhiriqi=['2012-01-01','2016-10-30']
data=zhangfu(qizhiriqi[0],qizhiriqi[1])
data.to_excel('result.xlsx')

