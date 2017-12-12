# -*- coding:UTF-8 -*-
def savfig(figureObj, fn_prefix1='backtest8', fn_prefix2='_1_'):
    import datetime    
    fmt= '%Y_%m_%d_%H_%M_%S'
    now = datetime.datetime.now()
    fname_savfig = fn_prefix1 + fn_prefix2 + now.strftime(fmt)+ '.png'
    figureObj.savefig(fname_savfig, facecolor=fig.get_facecolor())


def backtest8(ohlc=ohlc, SD=1.0, n_short=2, n_long=20, f_savfig=False):
    u'''
    双均线策略回测函数
    signature: backtest8(ohlc=ohlc, SD=1.0, n_short=2, n_long=20, f_savfig=False)
    param::
    ohlc      - dohlcva 数据, dataFrame结构的
    SD        - MA1/MA2 > SD 触发多头买入的快均线/慢均线的阀值
    f_savefig - flag for saving Matplot output figures
    
    
    
    '''
    import matplotlib 
    #import seaborn as sns
    #sns.set_style('white')
    
    myfontprops = matplotlib.font_manager.FontProperties(
                        fname='C:/Windows/Fonts/msyh.ttf')#微软雅黑
                        
    maShort = pd.Series.rolling(ohlc.C, n_short).mean()
    maLong  = pd.Series.rolling(ohlc.C, n_long).mean()

    
    fig=plt.figure() # create new figure
    ohlc.C.plot(grid=True, figsize=(8,4))
    maShort.plot(label='MA'+str(n_short))
    maLong.plot(grid=True,label='MA'+str(n_long))
#    ohlc.iloc[:,[0,1,2,3]].plot(grid=False, figsize=(8,4))
#    ohlc.iloc[:,[0,1,2,3]].plot(grid=True,figsize=(8,4))
    plt.legend(loc='best')
    plt.title( s=u'历史股价', fontproperties=myfontprops)
    if f_savfig:
        savfig(fig, 'backtest8', '_0_')
        
#    SD=1.0
    regime = np.where( maShort/maLong > SD, 1, 0)
    regime = pd.Series(regime, index=maShort.index)
    print ('Regime Length = %s'%regime.size)
        
    fig=plt.figure() # create new figure
    regime[:].plot(lw=1.5, ylim=(-0.1, 1.1), figsize=(8,4), title=u'Regime')
    if f_savfig:
        savfig(fig, 'backtest8', '_1_')
        
    fig=plt.figure() # create new figure
    regime[-100:].plot(lw=1.5, ylim=(-0.1, 1.1), figsize=(8,4), title=u'Regime')
    if f_savfig:
        savfig(fig, 'backtest8', '_2_')
    
    
    
    pp_ratio_bnh = np.log(ohlc.C / ohlc.C.shift(1) )
    pp_ratio_strategy = regime.shift(1) * pp_ratio_bnh
    #最后我们把每天的收益率求和就得到了最后的累计收益率
    #（这里因为我们使用的是指数收益率，所以将每日收益累加是合理的），
    #这个累加的过程也可以通过DataFrame的内置函数cumsum轻松完成： 
    norm_return_bnh      = pp_ratio_bnh     .cumsum().apply(np.exp)
    norm_return_strategy = pp_ratio_strategy.cumsum().apply(np.exp)
    
    fig=plt.figure() # create a new figure
    norm_return_strategy. plot(lw=1.5,  figsize=(8,4), label=u'Strategy')
    norm_return_bnh.      plot(lw=1.5, label=u'BnH')
    
    plt.legend(loc='best')
    plt.title(s=u'策略收益率与历史价格对比', fontproperties=myfontprops)
    if f_savfig:
        savfig(fig, 'backtest8', '_3_')
    
    assert (regime.index == ohlc.C.index).all()==True # 'signal index not equals price index'
    # assert用来判断语句的真假，如果为假的话将触发AssertionError错误, 为开发人员提示出错的表达式
    return norm_return_strategy, n_short, n_long, SD