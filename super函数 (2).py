encoding:utf8
# class A:
# 	def __init__(self):
# 		print 'enter A'
# 		print 'leave A'
# class B(A):
# 	def __init__(self):
# 		print 'enter B'  #打印enter B
# 		A.__init__(self) #打印enter A,打印leave A,使用非绑定的类方法（用类名来引用的方法），并在参数列表中，引入待绑定的对象（self），从而达到调用父类的目的
# 		print 'leave B'  #打印leave B
# B()

'''
这样做的缺点是，当一个子类的父类发生变化时（如类B的父类由A变为C时），必须遍历整个类定义，
把所有的通过非绑定的方法的类名全部替换过来

'''
class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, smaPeriod):
        super(MyStrategy, self).__init__(feed, 1000) #super的意思是去找strategy这个类的父类，调用里面的方法
        self.__position = None
        self.__instrument = instrument
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__sma = ma.SMA(feed[instrument].getPriceDataSeries(), smaPeriod)

    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        self.info("BUY at $%.2f" % (execInfo.getPrice()))






































