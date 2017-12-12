#encoding:utf8
#本程序想要实现的功能是:输入一个股票代码,取出这只近一个月的K线,取出一个长度是30的list
#作为比较K线的第一个参数


import matplotlib.pyplot as plt
from math import log,exp
import tushare as ts
import numpy as np
import pymongo
import random
conn = pymongo.MongoClient('localhost',27017)
db_adjusted = conn.stock_data_ten_years_adjusted
# ALL_CLOSE_PRICE = 'all_close_price'
#首先要从数据库db_adjusted里面取到一个list,就是每一只股票的价格list的倒数30个
collection = db_adjusted['sh600000']#先尝试连接一个表

for items in collection.find():
    list_one_all = (items['forward_adjusted_price'])
    tail_list = list_one_all[-30:]
    print(tail_list)
    list_without_tail = list_one_all[:-30]#取去除了最近的30个交易日的list,用这个list来进行拆分进行比较
    i = -31
    while -i+30<len(list_without_tail):
    # print(list_one_all)
        print(list_without_tail[i:i+30])
        i+=-1


def compare_k(list_one, list_two):
    log_max_list = []
    i = 0
    for i in range(len(list_one) - 1):  # 取出列表中的前n-1个元素，因为除了最后一个元素之外,其他都要作为分母
        denominator = list_one[i]  # 先取到列表中的第一个元素作为分母
        j = i + 1  # 先取到分母之后的第一个元素作为分子，固定住i,i++的逻辑已经在for语句里面了
        while j < len(list_one):# 当j不超过序列的长度时,打印值
            max_one = ((list_one[j] / list_one[i]) / (list_two[j] / list_two[i])) if ((list_one[j] / list_one[i]) / (list_two[j] / list_two[i]))>1 else ((list_two[j] / list_two[i]) / (list_one[j] / list_one[i]))
            j = j+1
            log_max_list.append(log(max_one))
    return (exp((sum(log_max_list)) / combination_num) - 1)
# def compare_k(list_one,list_two):#list_one是每一只股票代码,list_two是另外的3000只与之要对比的K线
#     log_max_list = []
#     i = 0
#     for i in range(len(list_one)-1):#取出列表中的前n-1个元素，因为除了最后一个元素之外,其他都要作为分母
#         j = i + 1 #先取到分母之后的第一个元素作为分子，固定住i,i++的逻辑已经在for语句里面了
#         while j < len(list_one):#当j不超过序列的长度时,打印值
#             max_one = ((list_one[j]/list_one[i])/(list_two[j] / list_two[i])) if ((list_one[j]/list_one[i])/(list_two[j] / list_two[i])) > 1 else ((list_two[j]/list_two[i])/(list_one[j] / list_one[i]))
#             j = j+1
#             log_max_list.append(log(max_one))
#             # print(log(max_one))
#     # print(sum(log_max_list))
#     # print(exp((sum(log_max_list))/combination_num)-1)#结果越接近0,说明两条曲线的相似度越高
#     # plt.plot(list_1)
#     # plt.plot(list_2)
#     # plt.plot(list_1_log)
#     # plt.plot(list_2_log)
#     # plt.show()
#     return(exp((sum(log_max_list))/combination_num)-1)
#
#
# # compare_k(list_1,list_2)
#
# for i in range(500000):
#     list_1 = []
#     price1 = 10
#     list_1.append(price1)
#     for i in range(30):
#         zhangdie = 0.1 * random.uniform(-1, 1)
#         price1 = price1 + price1 * zhangdie
#         list_1.append(price1)
#     list_1_log = [log(i) for i in list_1]
#     list_2 = []
#     price2 = 10.6
#     list_2.append(price2)
#     for j in range(30):
#         zhangdie = 0.1 * random.uniform(-1, 1)
#         price2 = price2 + price2 * zhangdie
#         list_2.append(price2)
#     list_2_log = [log(i) for i in list_2]
#     combination_num = (len(list_1) * (len(list_1) - 1)) / 2
#     s = compare_k(list_1,list_2)
#     print(s)
#     if s<0.06:
#         print(s)
#         plt.plot(list_1_log)
#         plt.plot(list_2_log)
#         plt.show()


# compare_k(list_1, list_3)

# print(db.collection_names())#打印表名
# posts = db.post
# # print(dir(posts))
# print(posts.count())
# for item in posts.find():
#     print(item)



def show_users(code):#这个函数实现我输入一个代码,返回给我3只最像的3条K线
    pass















































































































