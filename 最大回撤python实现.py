#encoding:utf8
import numpy as np

def max_drawdown(timeseries):
    # 回撤结束时间点
    i = np.argmax(np.maximum.accumulate(timeseries) - timeseries)
    # 回撤开始的时间点
    j = np.argmax(timeseries[:i])
    return (float(timeseries[i]) / timeseries[j]) - 1



result = max_drawdown([3.3,3,4,5,6])
print result