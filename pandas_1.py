# -*- coding:UTF-8 -*-
import pandas as pd
import datetime
import pandas.io.data as web
# import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2014, 2, 1)

df = web.DataReader("XOM","yahoo",start,end)
print df.head()
df['Adj Close'].plot()
plt.show()
