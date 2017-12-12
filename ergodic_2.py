for x in range(1,10):
	for y in range(1,10):
		print x*y

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
all_list = []    ################### in order to check out the numbers of this list
for i in range(len(x)):
	for j in range(len(y)):
		n = x[i] * y[j]
		all_list.append(n)
		all_list.sort()
	print all_list


