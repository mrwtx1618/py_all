# -*- coding:UTF-8 -*-
import urllib2
import numpy as np
import os
import MySQLdb
import time
import math
import xlrd
import pandas as pd
url='http://gw.yundzh.com/quote/kline?obj=SH000001&begin_time=20160822-000000-000-0&field=ShiJian,ShouPanJia&split=1&period=1day&token=00000010:1480574352:4eb889e79a639b556b585984acd4563d9ae9908e'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
f = f.read()
f = eval(f)
#f = f['Data']['JsonTbl']['data'][0][0]['data'][0][1]['data']
print f