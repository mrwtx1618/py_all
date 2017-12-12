# -*- coding:UTF-8 -*-
import urllib2
import numpy as np
import os
#import MySQLdb
import time
import math
import xlrd
import pandas as pd



def timetran(t):             #转换时间格式 时间戳
    timeStamp = t
    timeArray = time.localtime(timeStamp)
    t = time.strftime("%Y-%m-%d", timeArray)                                                                               #time.strftime()可以用来获得当前时间，可以将时间格式化为字符串等等
    return t
print timetran(123456789)

