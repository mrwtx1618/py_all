#encoding:utf8
from random import random
n = 10000
i = 0
count_x = 0
while i < n:
	x = random()
	if x > 0.6:
		count_x+=1
		print x
	i+=1	
print float(count_x)/i












