# -*- coding:UTF-8 -*-
#利用map函数计算3个字符串的长度
abc = ['com','fdsfs','ds']
print map(len,abc) #map函数把len这个函数依次作用于字符串abc上
#利用lambda和map函数来实现打印1到9的平方
result1 = map(lambda x:x*x,range(1,10)) #把lambda这个函数依次作用于range(1,10)之上
print result1
#计算一个数组中所有正数的和，用reduce,filter,lambda
n = [2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
result2 = sum(filter(lambda x:x > 0,n))
print result2
###代码更简单了
###数据集，操作，返回值都放到了一起
###你在读代码的时候，没有了循环体，于是就可以少了些临时变量，以及变量倒来倒去逻辑
###你的代码变成了在描述你要干什么，而不是怎么去干
###