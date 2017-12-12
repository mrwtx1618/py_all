#encoding:utf8
#这里主要讨论循环问题
#包括对字典、字符串的循环
#如何判断一个对象是否是可迭代对象
#如何打印对象以及索引本身

#打印字典里面的键
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
for keyy in d:
	print keyy

#对字符串的循环
for ch in 'ABCDEFGH':
	print ch

#所以，当我们准备使用for循环时，只要作用于一个可循环对象，
#for循环就可以正常执行，那么怎么判断一个对象是否是可迭代对象？
#方法是通过collections模块里的Iterable类型来判断

from collections import Iterable
print isinstance('abcdefg', Iterable)
print isinstance(12345, Iterable)

#for 循环其实可以同时使用两个甚至多个变量
#比如字典里的items()可以同时迭代key和value
d = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f',}
for k,v in d.items():
	print k,'=',v









































