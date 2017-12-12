#encoding:utf8
x = 'I am a global variable'
def fun():
	x = 100
	global y #强制把局部变量y转成全局变量，必须要在下面调用函数fun才能够global声明有意义
	y = 200
	print x
fun()
print x
print y