#encoding:utf8
#运用列表生成式，可以快速生成list
#可以通过list来生成另一个list，代码却十分简单
print (list(range(1,11)))

L1 = list(x*x for x in range(1,11)) #列表生成式
print (L1)

L2 = list(x*x for x in range(1,11) if x%2 == 0) #打印仅仅是偶数的平方
print (L2)

import os
print ([d for d in os.listdir('.')]) #os.listdir()可以列出文件和目录


#想把一个list里面所有的字符串变成小写
L3 = ['Hello','World','IBM','Apple']
L_lower = [s.lower() for s in L3] #通过一个list来生成另一个list
print (L_lower)




















