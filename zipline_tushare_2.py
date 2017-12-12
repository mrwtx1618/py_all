#encoding:utf8
#转换tushare中的数据格式，使得tushare中的数据格式与zipline中的数据格式相匹配
from collections import OrderedDict                                                                                                                                       
import tushare
from pandas import DataFrame, to_datetime
import pytz
from zipline import TradingAlgorithm
from zipline.finance.trading import TradingEnvironment
from zipline.finance import trading
from zipline.utils.factory import create_simulation_parameters
from zipline.api import order, record, symbol

SYMBOL = '399006' #创业板指

def get_data_from_tushare(stocks, start, end): #从tushare取数据的函数
    data = OrderedDict()
    for stock in stocks:
    	print stocks
        tushare_data = tushare.get_hist_data(stock, start = start , end = end)
        tushare_data.index = to_datetime(tushare_data.index).tz_localize(pytz.utc)
        data[stock] = tushare_data.sort_index()

    close_key = 'close'
    df = DataFrame({key: d[close_key] for key, d in data.iteritems()})
    df.index.name = 'Date'
    return df

# following lines come from zipline example in 'examples/buyapple.py' #这个策略是从zipline的例子里找的

def initialize (context,*args,**kwargs):
    pass

def handle_data(context, data):
    try:
        order(symbol(SYMBOL), 10) 
        record(**{SYMBOL: data[symbol(SYMBOL)].price})
    except:
        pass
def plot_function(results = None):
    import matplotlib.pyplot as plt
    from matplotlib import style
    style.use('ggplot') 
    # Plot the portfolio and asset data.
    ax1 = plt.subplot(211) #211表示2行1列两个子图，现在正在画第一个portfolio_value图,ax是一个Axes对象
    results['portfolio_value'].plot(ax=ax1,color = 'b', grid = True, linewidth = 1.6) # results的index是日期，根据输出的csv结果，有列名SYMBOL600111，algo_volatility,algorithm_period_return,alpha,benchmark_period_return,benchmark_volatility,beta,capital_used,ending_cash,ending_exposure,ending_value,excess_return,gross_leverage,information,long_exposure,long_value,longs_count,max_drawdown,max_leverage,net_leverage,orders,pnl,portfolio_value,positions,returns,sharpe,short_exposure,short_value,shorts_count,sortino,starting_cash,starting_exposure,starting_value,trading_days,transactions,treasury_period_return
    ax1.set_ylabel('Portfolio Performance') #把y轴命名为Portfolio Performance
    ax2 = plt.subplot(212, sharex = ax1) #取得另外一个Axes对象，212表示2行1列两个子图，现在正在画第二个get(SYMBOL)图
    results.get(SYMBOL).plot(ax = ax2, grid = True, linewidth = 1.6) #dataframe.get方法,SYMBOL可以改为
    ax2.set_ylabel('%s price ' % SYMBOL) #把第二个子图的名字命名为price，后面那个取SYMBOL的名字
    results.to_csv('aaaaaaaaaaaaaa.csv')

    # Show the plot.
    plt.gcf().set_size_inches(18, 8) # plt.gcf():Get a reference to the current figure.设置尺寸
    plt.show()

bars = get_data_from_tushare( # Using tushare to get data which could be handled by zipline later.
    stocks = [SYMBOL],
    start = "2015-10-09",
    end = "2016-02-07",
) #bars是一个DataFrame类型，索引就是日期，还有一列是'600111'的收盘价，从tushare调用数据


algo = TradingAlgorithm(
    initialize = initialize,
    handle_data = handle_data,
    identifiers=[SYMBOL]

)

perf = algo.run(bars) #performance是一个DataFrame类型
plot_function(results = perf) 