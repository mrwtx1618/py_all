# -*- coding:UTF-8 -*-
def jia(x,y):
	return x + y
if __name__ == "__main__": #这句话代表如果这个程序是被直接执行的话，这样的话，当别人调用这个模块时，就不会反复地执行里面的不必要的代码
	print jia(2, 3)
print __name__
print'In order to check whether print __main__ or not'