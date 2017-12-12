#encoding:utf8
import time
# def today():
# 	print time.strftime('%Y-%m-%d')
# f = today #由于函数也是一个对象，而且函数对象可以被赋值给变量
# f() #所以，通过变量也能调用该函数

# print f.__name__ ###函数对象有一个__name__属性，可以拿到函数的名字
'''
现在，假设我们要增强now()函数的功能。比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义。
这种在代码运行期间动态增加功能的方式，称之为装饰器(decorator)
本质上，
decorator是一个返回函数的高阶函数
'''
###log_是一个装饰器，接受一个函数作为参数，并且返回另一个函数
def log_(func):
	def wrapper(*args, **kw):
		print 'call %s():' %func.__name__
		return func(*args, **kw)
	return wrapper #返回了一个函数，打印call sth



@log_ #把@log_放到today()函数的定义处，相当于log_(today)
def today():
	print time.strftime('%Y-%m-%d')
f = today #由于函数也是一个对象，而且函数对象可以被赋值给变量
f() #所以，通过变量也能调用该函数




























