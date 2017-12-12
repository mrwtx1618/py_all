#encoding:utf8
#https://en.wikipedia.org/wiki/Pi Rate of convergence
from decimal import *
import os
from time import *
getcontext().prec = 50

s = Decimal(1)
pi = Decimal(3)

n = 5000 #注意到n=50000时程序大约运行8秒


for i in range(2, n  * 2, 2):
	pi = pi + s * (Decimal(4)/(Decimal(i)*(Decimal(i)+Decimal(1))*(Decimal(i)+Decimal(2))))
	s = -1 * s
	print "Apprpximate value of PI:",pi,"for",i
	sleep(0.5)

os.system('pause')









