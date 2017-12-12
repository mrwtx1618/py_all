#encoding:utf-8
import datetime
import matplotlib.pyplot as plt
#现在日期是一个由日期字符串组成的list,现在想把日期作为横轴来作图,并且把日期旋转45度方便阅读
fig1 = plt.figure(figsize=(10,8))
dates1= '2005-02-08'
dates2= '2005-02-09'
dates3= '2005-02-10'
dates4= '2005-02-11'
dates5= '2005-03-12'
dates1 = datetime.datetime.strptime(dates1,'%Y-%m-%d')
dates2 = datetime.datetime.strptime(dates2,'%Y-%m-%d')
dates3 = datetime.datetime.strptime(dates3,'%Y-%m-%d')
dates4 = datetime.datetime.strptime(dates4,'%Y-%m-%d')
dates5 = datetime.datetime.strptime(dates5,'%Y-%m-%d')
dates = [dates1,dates2,dates3,dates4,dates5]
print(type(dates))
# print(dates)
# # print(dates)
list_1 = [1,2,3,10,5]
ax = plt.plot(dates,list_1)
# for tick in ax.get_xticklabels():
#     tick.set_rotation(45)
# for labels in plt.
plt.xticks(rotation = 45)#旋转45
plt.show()
#返回了一个排序好的list的原来的下标
#
#
# print('获取数据完成！')


# names = '读者传媒'
# code= '603999'
# close_price = ts.get_hist_data('603999')['close']
# # print(close_price)
# dict_data = {}
# dict_data['names'] = names
# dict_data['code'] = code
# dict_data['close_price'] = close_price
# print(dict_data)
