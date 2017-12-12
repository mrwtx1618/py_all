#encoding:utf8
import numpy as np
def myfunc(a,b):
	if a > b:
		return a - b
	else:
		return a + b

vector_function = np.vectorize(myfunc)
result = vector_function([1,2,3,4],2)
print result













