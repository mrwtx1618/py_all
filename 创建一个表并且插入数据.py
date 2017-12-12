# -*- coding: UTF-8 -*-
#安装 MYSQL DB for python
import MySQLdb as mdb
import sys
 
#将 con 设定为全局连接
con = mdb.connect('localhost', 'root', '', 'test1');
with con:
 
#获取连接的 cursor，只有获取了 cursor，我们才能进行各种操作
    cur = con.cursor()
 
#创建一个数据表 writers(id,name)
#cur.execute("CREATE TABLE IF NOT EXISTS \
#Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
 
#以下插入了 5 条数据
cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
con.commit()
con.close()

