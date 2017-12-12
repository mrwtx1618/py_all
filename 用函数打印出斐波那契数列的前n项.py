#encoding:utf8
def Fibonacci(n):
	a,b,i = 0,1,0
	while i < n:
		a,b = b,a+b
		i+=1
		print b
Fibonacci(10)













