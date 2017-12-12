#encoding:utf-8
import tushare as ts
import pymongo
conn = pymongo.MongoClient('localhost',27017)
db = conn.tushare_data
ALL_CLOSE_PRICE = 'all_close_price'

# print(len(ts.get_today_all()['code']))#一共有3109只票
stock_names = ts.get_today_all()['name']#股票名列表
code = ts.get_today_all()['code']#股票代码列表
# print(len(stock_names))
# print(len(code))
close_price_list = []#收盘价列表
for code in ts.get_today_all()['code']:
    close_price = ts.get_hist_data('%s'%code,start='2016-09-20',end='2016-12-09')['close'].tolist()[::-1]
    # print(close_price)
    close_price_list.append(close_price)
for i in range(len(code)):
    print((close_price_list)[i])
# dict_list = []#构造一个list,list里面的元素是字典,每一条字典里面含有3条数据,分别是股票名称,
# for i in range(len(code)):
#     dict_data = {}
#     dict_data['code'] = code[i]
#     dict_data['name'] = stock_names[i]
#     if len(close_price_list[i]) < len(code):
#         continue
#     else:
#     # print(dict_data)
#         dict_data['close_price'] = close_price_list[i]
#     # print(dict_data)
#         dict_list.append(dict_data)
# print(dict_list)
# for item in dict_list:
#     db[ALL_CLOSE_PRICE].update_one({'code':item['code'],'name':item['name']},{'$set':item},upsert = True)
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
