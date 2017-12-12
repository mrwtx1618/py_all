#encoding:utf8
#现在想实现一个函数，想要完成的功能是当n是奇数是，打印weird,
#当n是偶数时，如果2<=n<=5,打印not weird
#当n是偶数时，如果6<=n<=20,打印weird
#当n>20时,打印not weird

def test_if_elif_else(n):
	if n%2 == 1:
		print "奇数" #这里的意思是只要n是奇数，那么就打印出“奇数”，如果是偶数在分情况讨论
	elif 2 <= n <= 5:
		print "Not Weird"
	elif 6 <= n <= 20:
		print "Weird"
	else:
		print "Not Weird"

for i in range(30):
	test_if_elif_else(i)


# test_if_elif_else(15)











































