#encoding:utf8
t = ('name','Tom') #现在t的类型是一个元组
d1 = {'age':30,'name':'Tom'} #d是一个字典,字典是无序的
d2 = {'name':'Tom','age':20} #所以可以交换字典内的顺序
d3 = {'a':30,'n':'Tom'}
def f1(x,y):
	print 'His %s is:%s'%(x,y)
f1(*t) #通过*号来把tuple类型的值传进去

def f2(name = 'name',age = 0):
	print 'name:%s'%name
	print 'age:%s'%age
f2(**d1)
f2(**d2) #通过两个星号把字典类型的值传进去
f2(**d3) #这个会报错，因为key对不上
f2(d3['n'],d3['n'])