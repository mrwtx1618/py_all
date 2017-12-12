#encoding:utf8
from os import getpid
from multiprocessing import Process
from time import sleep

def prove_existence():
	print getpid() #获得当前进程的进程号,process id

if __name__ == '__main__':
	p1 = Process(target=prove_existence, args = ())
	p1.start()
	p1.join()
	p2 = Process(target=prove_existence, args = ())
	p2.start()
	p2.join()

#It creates a new process and it actually works. 
#Because there two process id.
















