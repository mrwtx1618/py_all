#encoding:utf8
from time import sleep
from multiprocessing import Pool
def start_function_for_processes(n):
	sleep(0.2)
	result_sent_back_to_parent = n * n
	return result_sent_back_to_parent
if __name__ == '__main__':
	p = Pool(processes=5)
	results = p.map(start_function_for_processes, range(100001), chunksize = 10) #chunksize = 10:块大小， pass 10 items at a time
	print results

#python 3中的写法：with Pool(processes=5) as p:











