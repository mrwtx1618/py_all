#encoding:utf-8

#注意到*args返回的是一个tuple
import random


def test(the_first_arg,*args):
	print(the_first_arg,args)
	print(args)
	for the_arg in args:
		print(the_arg)

# test(1,2,3,4,5)


#比如现在有一个list:想打印这个list里面的所有的值,通常这个list的长度是不确定的

test_list = range((random.randint(1,10)))#这是一个可变长度的随机list
# print(test_list)
test_tuple = tuple(test_list)
print(test_tuple)

def test_args(*args):#可变参数传入的是一个tuple
	for the_arg in args:
		print(the_arg)

test_args(test_tuple)
















