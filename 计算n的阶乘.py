def factorial_if(n):
	if n > 0:
		result = n * factorial_if(n - 1)
		n = n - 1
	print result
factorial_if(5)