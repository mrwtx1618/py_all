#encoding:utf8
f1 = lambda x:x**2 #lambda语句构建的是一个函数对象
f2 = lambda x,y:x * y
print f1(6)
print f2(8,9)
print type(f1)
print id(f1)