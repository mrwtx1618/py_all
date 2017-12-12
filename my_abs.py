#encoding:utf-8
#定义一个自己的abs函数
# def my_abs(x):
# 	if x>=0:
# 		return x
# 	else:
# 		return -x
# result = my_abs('A') #这里改成了A这样一个字符串，结果还是A，并没有报错，所以这个函数的定义并不完善
# print result

#空函数，如果想定义一个什么事也不做的空函数，可以用pass函数
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来，以保持程序结构的完整性
# def nop():
# 	pass

# def my_abs(x):
# 	if not isinstance(x, (int,float)):
# 		raise TypeError('bad operand type')
# 	if x >= 0:
# 		return x
# 	if x < 0:
# 		return -x
# print my_abs(-0.443)

#函数返回多个值，函数可以返回多个值嘛？答案是肯定的
#比如从一个点移动到另一个点，给出一个点的坐标，位移和角度，要返回出新的坐标
# import math
# def move(x,y,dist,angle):
# 	nx = x + dist * math.cos(angle)
# 	ny = y - dist * math.sin(angle)
# 	return nx,ny
# print move(100, 100, 60, math.pi/6)
# print type(move(100,100,60,math.pi/6))#It is a tuple

# ###定义一个函数有两个参数，来计算任何n次方
# def power(x,n = 2): #通过设定n = 2把第二个参数的默认值设定为2
# 	s = 1
# 	while n > 0:
# 		n = n - 1
# 		s = s * x
# 	return s
# print power(6)

#可变参数，在Python函数中，还可以定义可变参数。可变参数就是传入的参数的个数是可变的
#可以是1个、2个到任意个，还可以是0个
#以数学题为例子，给定一组数字a,b,c......,计算a^2+b^2+c^2+......
#要定义出这个函数，我们必须确定输入的参数
#由于参数个数不确定，我们首先想到可以把a,b,c,......作为一个list或tuple传进来

# def calc(numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n * n
# 	return sum
# ###但是在调用的时候，需要先组装出一个list或者tuple
# print calc([1,2,3])

###如果利用可变参数，调用函数的方式就可以简化
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n * n
# 	return sum
# print calc(1,2,3,4),calc(1,2),calc()

###关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装成一个tuple
#而关键字参数允许你传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装成一个dict

# def person(name,age,**kw):
# 	print 'name:',name,'age:',age,'other:',kw
# print person('Peter', 19)

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
#也可以传入任意个数的关键字参数
# print person('Bob', 18, city = 'Shanghai')
#关键字参数可以扩展函数的功能
#比如，在person函数里，我们保证能接收到name和age这两个参数
#但是，如果调用者愿意提供更多的参数，我们也能够收到
#试想你正在做一个用户注册的功能，除了用户名和年龄是必须的以外，其他的都是可选项
#利用关键字参数来定义这个函数就能满足注册的需求
#参数组合
#在Python中定义函数，可以用必选参数，默认参数，可变参数和关键字参数
#这4中参数都可以一起使用，或者只用其中一些
#但是请注意，参数的定义顺序必须是：必选参数，默认参数，可变参数和关键字参数
#比如定义一个函数，包含上述4中参数：
# def func(a, b, c = 0, *args, **kw):
# 	print 'a = ',a, 'b = ',b, 'c = ',c, 'args=',args,'kw=',kw
# func(1, 2)
# func(1, 2,3,'a','b')
# func(1, 2,3,'a','b','c', x = 99)
#最神奇的是通过一个tuple和dict，也可以调用该函数
# args = (1,2,3,4)
# kw = {'x':99}
# func(args, kw)

###传入函数
#既然变量可以指向函数，函数的参数能够接收变量，那么一个函数就可以接收另一个函数作为参数
#这种函数就成为高阶函数
#一个简单的高阶函数：
# def add(x,y,f):
# 	return f(x)+f(y)
# print add(3, -1, abs)

###  map & reduce
#Python内建了map()和reduce()函数
#先看map，map()函数接收两个参数，一个是函数，一个是序列
#map()将传入的函数一次作用到序列的每个元素，并把结果作为新的list返回
# def f(x):
# 	return x*x
# result_1 = map(f, [1,2,3,4,5,6,7,8,9,10])
# result_2 = map(str, [1,2,3,4,5,6,7,8,9,10])#把这个list里面所有数字转化成字符串，只要一行代码
# print result_2

#再看reduce的用法，reduce把一个函数作用在一个序列[x1,x2,x2,...]上
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积运算
#比方说要对一个序列求和，就可以用reduce实现：
# def add(x,y):
# 	return x + y
# result = reduce(add, [1,2,3,4,5])
# print result
#Python内建的filter()函数用来过滤序列
#和map类似，filter()也接收一个函数和一个序列
#和map不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是Flase来决定丢弃还是保留该元素
#例如在一个list中，要删掉其中的偶数，保留奇数
# def keep_even(n):
# 	return n % 2 == 1
# result_3 = filter(keep_even, [1,2,3,4,5,6,7])
# print result_3

###返回函数
#函数作为返回值
#高阶函数除了可以接受函数作为参数以外，还可以把函数作为结果值返回
#我们来实现一个可变参数的求和，通常情况下，求和函数是这样定义的：
# def calc_sum(*args):
# 	ax = 0
# 	for n in args:
# 		ax = ax + n
# 	return ax
# result_4 = calc_sum(1,2,3,4,5)
# print result_4

#但是，如果不需要立刻求和，根据需要再计算怎么办？可以不反悔求和的结果，而是返回求和的函数
def lazy_sum(*args):
	def my_sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
#当我们调用lazy_sum时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1,2,3,4,5)
print f









