# encoding:utf8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create random walk which I want to calculate maximum drawdown for:
T = 50
mu = 0.05
sigma = 0.2
S0 = 20
dt = 0.01
N = int(round(T / dt, 0))  # 加上int是把5000.0变成5000
t = np.linspace(0, T, N)  # linspace()通过指定开始值、终值、和元素个数创建表示等差数列的一维数组，现在t是一个表示等差数列的一维数组
a = np.random.standard_normal(size=N)
std_Bt = np.cumsum(a) * np.sqrt(dt)  # 标准布朗运动
X = (mu - 0.5 * sigma ** 2) * t + sigma * std_Bt  # 放在肩膀上的
geo_Bt = S0 * np.exp(X)
plt.plot(geo_Bt)
plt.show()


# Max drawdown function 最大回撤函数
def max_drawdown(P):  # 这里K是一个参数序列,这里K就是所要分析的序列的高度，i.e.股价
    mdd = 0  # mdd是最大回撤率，首先假设最大回撤是0
    peak = P[0] #先假设peak是序列开始的高度
    for x in P:
        if x > peak:
            peak = x
        dd = (peak - x) / peak  # dd是最大回撤率
        if dd > mdd:
            mdd = dd
        return mdd


drawSeries = max_drawdown(geo_Bt)
print drawSeries
# MaxDD = abs(drawSeries.min() * 100)
# print MaxDD
# print drawSeries


