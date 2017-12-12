
# -*- coding:UTF-8 -*-
"""本程序想要实现查看一个股票高开0.8%之后低走的概率"""
"""取得日期为2015-8-31到2016-9-23"""
import tushare as ts
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime
import time
IV_1 = ts.get_today_all()
All_code = IV_1[['code']]
All_codes = pd.np.array(All_code)
All_codes = All_codes[:5]
for stocks in All_codes:
    IV_2 = ts.get_hist_data(stocks[0], ktype = 'D', start = '2015-08-31', end = '2016-09-23')
    Open_And_Close_Price = IV_2[['open','close']].copy()
    IV_3 = IV_2[['open','close']].copy()                                                                       #Take all the prices
    Market_Days = list(IV_3.index)     #取交易日
    Pre_Market_Days = [Market_Days[Market_Days.index(x)+1] for x in list(Market_Days)[:-1]]
    Market_Days = Market_Days[:-1]
    if Market_Days == []:
        continue
    else:
        print stocks[0]
        Price_Open_Array = []
        for i in Market_Days:
            Price_Open = Open_And_Close_Price['open'][str(i)]
            Price_Open_Array.append(round(Price_Open,2))
        #print Price_Open_Array
        Price_Close_Array = []
        for j in Market_Days:
            Price_Close = Open_And_Close_Price['close'][str(j)]
            Price_Close_Array.append(round(Price_Close,2))
        Price_Multiplied_Array = []
        for k in Pre_Market_Days:
            Price = Open_And_Close_Price['close'][str(k)]
            Price_M = Price * 1.008
            Price_Multiplied_Array.append(round(Price_M,2))
        #print Price_Multiplied_Array
        df = pd.DataFrame({'Price_Close':Price_Close_Array,'Price_Open':Price_Open_Array,'Price_Multiplied':Price_Multiplied_Array})
        df['Higher'] = df.Price_Open > df.Price_Multiplied
        Higher_Ones = df[(df.Price_Open > df.Price_Multiplied)]
        Denominator_Self = float(len(Higher_Ones))
        Falling_Ones = df[(df.Price_Open > df.Price_Multiplied)&(df.Price_Close < df.Price_Open)]
        Numerator_Self = float(len(Falling_Ones))
        #Numerator = 0
        #Numerator = Numerator + Numerator_Self
        #Denominator = 0
        #Denominator = Denominator + Denominator_Self
        #Probability = Numerator/Denominator
        print Numerator
        print Denominator
        print Probability
        
