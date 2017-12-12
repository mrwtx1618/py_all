#encoding:utf8
f1 = open('test.txt')
data = f1.read()
f1.close()
print data


#这里有两个问题。一是可能忘记关闭文件句柄；
#二是文件读取数据发生异常，没有进行任何处理。下面是处理异常的加强版本：

f2 = open('aaa.jpg')
try:
	data = f2.read()
	print data
finally:
	f2.close()

#虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了。
#除了有更优雅的语法，with还可以很好的处理上下文环境产生的异常。下面是with版本的代码

with open('test.txt') as f3:
	data = f3.read()
	print data





























































