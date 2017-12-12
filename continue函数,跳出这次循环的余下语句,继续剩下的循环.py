# -*- coding:UTF-8 -*-
for x in range(1,11):
	print x
	if x == 2:
		print 'hello 2' #加上了continue之后，希望得到的效果是hello 2以后不出现星号
		continue
	if x == 6:
		break        #这里break之后，后面的else语句的内容就不执行了
	print '*' * 10
else:
	print 'ending'
for x in range(1,11):
	print '----------------->',x
