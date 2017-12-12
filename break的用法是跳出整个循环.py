# -*- coding:UTF-8 -*-
for x in range(1,11):
	print x
	if x == 6:
		break        #这里break之后，后面的else语句的内容就不执行了，因为这里程序是非正常结束的。所以不执行else下的语句。
	print '*' * 10
else:
	print 'ending'
for x in range(1,11):
	print '----------------->',x

