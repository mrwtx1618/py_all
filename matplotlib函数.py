#encoding:utf8

import matplotlib.pyplot as plt
from math import log,e
from matplotlib.ticker import FuncFormatter
x_pos=[1,2,3,4,5]
y_pos=[1,2,3,4,5]
fig1=plt.figure() #这时候会产生一张图
ax=fig1.add_subplot(2,1,1)
ax.plot(x_pos,y_pos)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos=None:e**x))
ax.set_yscale('log')#设为对数坐标
ax2=fig1.add_subplot(2,1,2)
ax2.plot(x_pos,y_pos)



fig2 = plt.figure() #这时候会产生另外一张图

plt.show()