#encoding:utf8

import os

fileName = 'test_path.txt' #VT_setting.json里面共有5个字段，"fontFamily": "微软雅黑","fontSize": 12,"mongoHost": "localhost","mongoPort": 27017,"darkStyle": true
path = os.path.abspath(os.path.dirname(__file__)) #path是C:\Users\Administrator\Desktop\vnpy-master\vnpy-master\vn.trader
fileName = os.path.join(path, fileName) #fileName是C:\Users\Administrator\Desktop\vnpy-master\vnpy-master\vn.trader\VT_setting.json
f = file(fileName)
print type(f)