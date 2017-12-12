# -*- coding:UTF-8 -*-
a = 123
print id(a)
a = 456
b = 456
print id(a)
print id(b)
print id(3)



#a,b是两个不同的变量，但是引用的数据是同一地址的数据。
#返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。
#注：一个对象的id值在CPython解释器里就代表它在内存中的地址（Python的c语言实现的解释器）