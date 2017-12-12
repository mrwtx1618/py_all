# -*- coding:UTF-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
def dateRange(start, end):# 定义一个函数叫做dateRange，在给定两个日期之后，取出这两个日期的之间的所有日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1 #datetime.datetime.strptime(date_string, format),将格式字符串转换为datetime对象,现在是计算出了两个日期之间的天数
    print [datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(i), "%Y-%m-%d") for i in xrange(days)]
    print days
dateRange('2000-01-01', '2016-10-01')

###先返回出两个日期之间的天数
###strftime把datetime格式变成str格式，即最后会打印出一个字符串。
###但是函数传入的是一个字符串，所以要先用strptime格式来转成一个datetime格式
