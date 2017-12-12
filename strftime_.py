# -*- coding:UTF-8 -*-
import datetime
print datetime.datetime.now()
print type(datetime.datetime.now())
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')# striftime把datetime格式转成了字符串。Y大写，年的格式变成了2016，小写是16
print type(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))