#encoding:utf8
#本程序想要实现的功能是:输入一个股票代码,取出这只近一个月的K线,取出一个长度是30的list
#作为比较K线的第一个参数


import matplotlib.pyplot as plt
from math import log,exp
import tushare as ts
import numpy as np
import pymongo
import random
from matplotlib import font_manager#想在图片中输出中文,需要用到这个
import datetime #引入这个模块是因为要把日期的str格式编程datetime格式




zh_font = font_manager.FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)
conn = pymongo.MongoClient('localhost',27017)
db_adjusted = conn.stock_data_ten_years_adjusted_divided_by_2
# ALL_CLOSE_PRICE = 'all_close_price'
#首先要从数据库db_adjusted里面取到一个list,就是每一只股票的价格list的倒数30个
# collection = db_adjusted['sh600000']#先尝试连接一个表
#首先要定义一个函数,完成下面的任务：
#接受一个sh股票代码,返回一个tail_list和一个由30个元素的小list组成的大的list
def code_to_2_list(code):#
    collection = db_adjusted['%s'%code]  # 先尝试连接一个表
    for items in collection.find():
        stock_name = items['name']#取出这只股票的股票名
        list_one_all = [round(i,2) for i in items['avg_price_divided_2_price']]
        list_date_all = items['date']#取出了所有的日期
        tail_date_list = list_date_all[-30:]
        tail_list = list_one_all[-30:]#取最近的30个交易日的数据,这个list是用户输入的参数
        print(tail_list)
        list_without_tail = list_one_all[:-30]#取去除了最近的30个交易日的list,用这个list来进行拆分进行比较
        list_without_tail_list = []
        print(list_without_tail)
        i = -31
        print(len(list_without_tail))
        while -i+30<len(list_without_tail):
        # print(list_one_all)
            print(list_without_tail[i:i+30])
            # list_without_tail_log = [log(j) for j in list_without_tail[i:i+30]]
            list_without_tail_list.append(list_without_tail[i:i+30])
            i+=-1
        # print(list_without_tail_list[i])
        return tail_list, list_without_tail_list, stock_name,tail_date_list

tail_list,list_without_tail_list, stock_name,tail_date_list = code_to_2_list('sh600000')
# tail_list_log = [log(i) for i in tail_list]
# plt.plot(tail_list)
# plt.show()
for i in range(len(list_without_tail_list)):
    print(list_without_tail_list[i])

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
s_list = []
for i in range(len(list_without_tail_list)):
#     print(list_without_tail_list[i])
    # list_1 = []
    # price1 = 10
    # list_1.append(price1)
    # for i in range(30):
    #     zhangdie = 0.1 * random.uniform(-1, 1)
    #     price1 = price1 + price1 * zhangdie
    #     list_1.append(price1)
    # list_1_log = [log(i) for i in list_1]
    # list_2 = []
    # price2 = 10.6
    # list_2.append(price2)
    # for j in range(30):
#         zhangdie = 0.1 * random.uniform(-1, 1)
#         price2 = price2 + price2 * zhangdie
#         list_2.append(price2)
#     list_2_log = [log(i) for i in list_2]
    combination_num = (len(tail_list) * (len(tail_list) - 1)) / 2
#     # print(combination_num)
    s = compare_k(tail_list,list_without_tail_list[i])
    s_list.append(s)
s_list_sort = sorted(s_list)
print(s_list)
print(s_list_sort)
    # print(s)
#     print(s)
s_list_sort = s_list_sort[:3]
print(s_list_sort)
print(tail_date_list)
tail_date_datetime_list = [datetime.datetime.strptime(single_dates,'%Y-%m-%d') for single_dates in tail_date_list]
i_list = []#定义一个下边列表
for num_3 in s_list_sort:
    for i in range(len(s_list)):
        if num_3==s_list[i]:
            i_list.append(i)

print(i_list)
for i in i_list:
    # if s<0.012:
    # print(s)
    print(tail_list)
    print(i)
    print(list_without_tail_list[i])
    tail_list_log = [log(i) for i in tail_list]
    list_without_tail_log = [log(j) for j in list_without_tail_list[i]]
    # print(list_without_tail_log)
    fig1 = plt.figure(figsize=(10,8))#先创建第一幅图,构想为这幅图分为两部分,subplot(2,1,1)为最近30天的K线,subplot(2,1,2)为相似的K线，figsize来设置
    ax_up = fig1.add_subplot(2,1,1)#先做两幅图之间的上面的那幅图
    ax_up.plot(tail_date_datetime_list,tail_list)#先做用户选定的那条K线,传入日期以及价格
    plt.xlabel('%s'%stock_name,fontproperties=zh_font)
    ax_down = fig1.add_subplot(2,1,2)#再做两幅图之间的下面的那幅图
    ax_down.plot(list_without_tail_list[i])
    plt.xlabel('sss')
    # plt.plot(tail_list)
    # plt.plot(list_without_tail_list[i])
    plt.show()


# compare_k(list_1, list_3)

# print(db.collection_names())#打印表名
# posts = db.post
# # print(dir(posts))
# print(posts.count())
# for item in posts.find():
#     print(item)



def show_users(code):#这个函数实现我输入一个代码,返回给我3只最像的3条K线
    pass















































































































