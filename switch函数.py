# -*- coding:UTF-8 -*-
#python当中没有switch这个语句，但是可以通过字典来实现switch功能
from __future__ import division #加入这个模块，除法可以直接实现
def add(x,y):
	return x + y
def subtract(x,y):
	return x - y
def multiply(x,y):
	return x * y
def divide(x,y):
	return x/y
def operator(x,o,y):
	if o == "+":
		print add(x, y)
	elif o == '-':
		print subtract(x, y)
	elif o =='*':
		print multiply(x, y)
	elif o == '/':
		print divide(x, y)
	else:
		pass
z = operator(5, '/', 8)
# print z
###但是以上这种办法，比如要做除法运算，上面的三次判断都是多余的,所以想用字典的办法来解决问题
operator_dict = {'+':add,'-':subtract,'*':multiply,'/':divide}
print type(operator_dict['+']) #这时候通过加号这个键取到的值是一个函数对象
print operator_dict['+'](3,9)
print operator_dict.get('*')(3,9) #字典下面有get这个方法来获取key，通过字典来调用函数
def f1(x,o,y):
	print operator_dict.get(o)(x,y)
f1(5, '/', 8) #调用函数
f1(6, '*', 6) #这时候已经没有判断了
###但如果用户所输入的字符不在字典里面的？
###通过可变参数来接收用户传入的多余的值
def f2(x,o,y):
	print operator_dict.get(o)(x, y, *args, **kwargs)
f2(4, '*', 3)
###一般的if结构都可以通过字典+switch结构来实现












