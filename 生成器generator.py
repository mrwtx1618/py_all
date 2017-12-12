#encoding:utf8
#通过列表生成式,可以直接来创建一个list
#但是，受到内存的限制，列表的容量是有限制的
#而且，如果创建了一个含有100万元素的list，但是只只访问几个元素的话
#就会浪费很大的内存空间
#现在想做的是，不创建完整的list， 而是一边循环一边计算
#这种机制叫做生成器:generator
#方法很简单:把[]改成()
# L = [x*x for x in range(1,11)]
# print L
# g = (x*x for x in range(1,11))
# print g
# print next(g)
# for n in g: #generator也是可迭代对象
# 	print n

# def Fibonacci(n):
# 	a,b,i = 0,1,0
# 	while i < n:
# 		print b
# 		a,b = b,a+b
# 		i+=1
# 		# print b
# Fibonacci(10)


#可以看出，Fibonacci()函数实际上定义了该数列的运算规则，
#可以从第一个元素开始，推算出后面的任意的元素，
#这种逻辑实际上很类似于generator
#而把Fibonacci()函数改成generator,只要把print b改成yield b


def Fibonacci_yield(n):
	a,b,i = 0,1,0
	while i < n:
		yield b
		a,b = b,a+b
		i+=1
		# print b
print Fibonacci_yield(10) #这个函数里面的代码并没有真正运行
                          #仅仅是返回了一个生成器对象

for number in Fibonacci_yield(10): #generator也是可以迭代的
	print number

#这里Fibonacci_yield()是一个generator(生成器)
#Generators(生成器)也是可迭代的，但是你每次只能迭代它们一次，
#因为不是所有的迭代器都被一直存储在内存中的，他们临时产生这些值


