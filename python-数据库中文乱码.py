#encoding=utf-8
import sys
import MySQLdb
# reload(sys)
# sys.setdefaultencoding('utf-8')
con = MySQLdb.connect('localhost','root','','sto',charset='utf8')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS \
	Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
cur.execute("INSERT INTO Writers(Name) VALUES('ff')")
cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
cur.execute("INSERT INTO Writers(Name) VALUES('kk')")
cur.execute("INSERT INTO Writers(Name) VALUES('张三峰')")
con.commit()
