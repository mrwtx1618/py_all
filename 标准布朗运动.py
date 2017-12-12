#encoding:utf8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create random walk which I want to calculate maximum drawdown for:
T = 50
mu = 0.05
sigma = 0.2
S0 = 20
dt = 0.01
N = int(round(T / dt, 0)) #加上int是把5000.0变成5000
t = np.linspace(0,T,N) #linspace()通过指定开始值、终值、和元素个数创建表示等差数列的一维数组，现在t是一个表示等差数列的一维数组
a = np.random.standard_normal(size = N)
std_Bt = np.cumsum(a) * np.sqrt(dt) #标准布朗运动
plt.plot(std_Bt)
plt.show()















