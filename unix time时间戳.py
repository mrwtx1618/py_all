#encoding:utf8
import datetime
import time
import numpy as np
# print time.time() #打印出了unix time,unix时间戳是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒。
# print datetime.datetime.fromtimestamp(time.time())
dateconv = np.vectorize(datetime.datetime.fromtimestamp)
date = dateconv(2017-01-01)
print date










