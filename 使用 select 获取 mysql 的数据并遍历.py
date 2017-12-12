# -*- coding: UTF-8 -*-
#安装 MYSQL DB for python
import MySQLdb as mdb
import sys
 
#连接 mysql，获取连接的对象
con = mdb.connect('localhost', 'root', '', 'test1');
with con:
 
#仍然是，第一步要获取连接的 cursor 对象，用于执行查询
    cur = con.cursor()
 
#类似于其他语言的 query 函数， execute 是 python 中的执行查询函数
cur.execute("SELECT * FROM Writers")
 
#使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
rows = cur.fetchall()
 
#依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
for row in rows:
    print row
