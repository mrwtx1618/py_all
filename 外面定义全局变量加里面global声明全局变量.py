#encoding:utf8
x = 'I am global variance'
def fun():
	global y
	y = 200
	global x
	x = 100
print x
fun()
print x
#上面的print x的运行结果是 I am global variance
#下面的运行结果是100
#因为下面的结果是在调用了函数fun之后的结果。
