#encoding:utf-8
def fun(x,y):
	if x == y:
		print x,'=',y
	else:
		print x,'!=',y
s1 = raw_input('input a price:')
s2 = raw_input('input a flavor:')
def machine(x = 3,y = '奶油'): #奶油口味以及3元是默认参数
	print '生成一个',x,'元',y,'口味的冰激凌！'
machine(s1, s2)