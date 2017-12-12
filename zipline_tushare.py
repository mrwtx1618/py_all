# -*- coding:UTF-8 -*-
from collections import OrderedDict #有序字典                                                                                                                                       
import tushare
import pandas
import zipline
from pandas import DataFrame, to_datetime
import pytz                                     #pytz,time zone:python时区设置
from zipline import TradingAlgorithm
from zipline.api import order, record, symbol

SYMBOL = '399006'                               #取创业板指
tushare_data = tushare.get_hist_data('399006', start = '2014-12-01', end = '2014-12-31') #tushare_data是一个dataframe格式 
tushare_data.index = to_datetime(tushare_data.index).tz_localize(pytz.utc) #把pandas.core.index.Index格式转换成pandas.tseries.index.DatetimeIndex格式,pytz是一个与时区有关的模块
print tushare_data.sort_index()
help (zipline.TradingAlgorithm)
close_key = 'close'



# def load_bars_from_tushare(stocks, start, end):
#     data = OrderedDict()
#     for stock in stocks:
#         tushare_data = tushare.get_hist_data(stock, start = start , end = end)
#         tushare_data.index = to_datetime(tushare_data.index).tz_localize(pytz.utc)
#         data[stock] = tushare_data.sort_index()

#     close_key = 'close'
#     df = DataFrame({key: d[close_key] for key, d in data.iteritems()})
#     df.index.name = 'Date'
#     return df


# # following lines come from zipline example in 'examples/buyapple.py' #

# def initialize (context):
#     pass

# def handle_data(context, data):
#     order(symbol(SYMBOL), 10) 
#     record(**{SYMBOL: data[symbol(SYMBOL)].price})

# def analyze(results=None):
#     import matplotlib.pyplot as plt 
#     # Plot the portfolio and asset data.
#     ax1 = plt.subplot(211)
#     results.portfolio_value.plot(ax=ax1)
#     ax1.set_ylabel('Portfolio value (RMB)')
#     ax2 = plt.subplot(212, sharex=ax1)
#     results.get(SYMBOL).plot(ax=ax2)
#     ax2.set_ylabel('%s price (RMB)' % SYMBOL)

#     # Show the plot.
#     plt.gcf().set_size_inches(18, 8)
#     plt.show()

# bars = load_bars_from_tushare( # Using tushare to get data which could be handled by zipline later.
#     stocks = [SYMBOL],
#     start = "2014-01-01",
#     end = "2014-12-31",
# )

# algo = TradingAlgorithm(
#     initialize = initialize,
#     handle_data = handle_data,
#     identifiers=[SYMBOL]
# )

# perf = algo.run(bars)
# analyze(results = perf)     
# print bars