#encoding:utf8
#这里的pymysql是用在python3里面的

import pymysql
conn = pymysql.connect(host = '192.168.1.119', port = 3306, user = 'wind', passwd = '123456', db = 'wind')
cur = conn.cursor()
print(cur)
# cur.execute("SELECT obj, shoupanjia, FROM_UNIXTIME(shijian,'%Y-%m-%d') FROM kline")
# cur.execute("SELECT obj, shoupanjia, FROM_UNIXTIME(shijian,'%Y-%m-%d') FROM kline")
# list_r = []
# for r in cur.fetchall():
#     list_r.append(r)
# for i in range(len(list_r)):
#     print(type(list_r[i][0]))


import pymysql







# conn = pymysql.connect(host = '192.168.1.114',port = 3306,user = 'wind',passwd = 'wind',db = 'wind')
conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',passwd = '',db = 'stock_3000')
cur = conn.cursor()
#使用execute方法来执行SQL语句
# data = cur.execute("SELECT trade_dt,S_INFO_WINDCODE,S_VAL_MV"
#                    "FROM wind.ashareeodderivativeindicator"
#                    "WHERE trade_dt BETWEEN '20130101' AND '20130126' ")
length_of_rows = cur.execute("SELECT * FROM stock_3000.kline WHERE id=1")#这个返回的是受影响的行数
print('受影响的行数为{}行'.format(length_of_rows))
row_1 = cur.fetchone()
print(row_1)