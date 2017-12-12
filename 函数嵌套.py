#encoding:utf8
def f1(a,b):
	def f2(a):
		return 2 * a
	return f2(a) + b
print f1(5, 2)

#函数运行的顺序为：函数在def定义时并不会运行，
#运行到print f1(5,2)时会调用到f1函数，在f1函数里面，定义f2函数时不会运行f2函数
#当运行到return f2(a) + b时会调用到f2函数，返回10，最后的结果是12






















































