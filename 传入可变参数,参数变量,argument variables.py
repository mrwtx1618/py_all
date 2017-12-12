#encoding:utf8
def f(x,*args,**kwargs): #args是一个tuple类型，用来装传入的多余的参数,元组格式是一个星号，字典格式是两个星号
	print x
	print args
	print kwargs
f(2)
f(2,3,4,5,6)
f(2,3,4,5,6,y = 7)
f(x = 1, y = 2) #y = 2这个值会被放到字典中
f(1,2,3,4,5,6,x = 0,y = 10, z = 20)
f(1,2,3,4,5,6,y = 10, z = 20)