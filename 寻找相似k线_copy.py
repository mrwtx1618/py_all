#encoding:utf-8
import matplotlib.pyplot as plt
from math import log,exp
import tushare as ts
import numpy as np
import pymongo
import random
conn = pymongo.MongoClient('localhost',27017)
db = conn.tushare_data
ALL_CLOSE_PRICE = 'all_close_price'


#[1,2,3,4]和[2,3,4,5]是把[1,2,3,4]向上平移了一个单位,但是涨幅是不一样的
#[1,2,3,4]和[2,4,6,8]的涨幅是一样的！都是每次上涨100%
# list_1 = []
# price1 = 10
# list_1.append(price1)
# for i in range(200):
#     zhangdie = 0.1*random.uniform(-0.5,0.5)
#     price1 = price1+price1*zhangdie
#     list_1.append(price1)
#
#
# list_2 = []
# price2 = 10
# list_2.append(price2)
# for j in range(200):
#     zhangdie = 0.1*random.uniform(-0.5,0.5)
#     price2 = price2+price2*zhangdie
#     list_2.append(price2)
#
# print(list_1)
# print(list_2)



###################订制的k线
# list_1 = [1,2.01,2.5,3,5,6,7,8,9.4,8,9,8,7.2,6.5,6.8,7.1,7.5,6]
# list_2 = [1.99,4,5,6,10,12.1,14,16,18.9,15.8,18.6,15.9,14,13.1,13.5,14.2,15,12]

##################完全不像的情形
# list_1 = list(5*np.logspace(0,9,10,base=1.05))
# list_2 = list(5*np.logspace(0,9,10,base=0.95))
# print(list_1)
# print(list_2)

# list_1_log = [log(i) for i in list_1] #取对数坐标轴
# list_2_log = [log(i) for i in list_2]
# # list_3_log = [log(i) for i in list_3]
# combination_num = (len(list_1)*(len(list_1)-1))/2
# # print(combination_num)
# #首先要得到列表的长度n,后面计算组合数以及对列表进行循环都需要这个数字
#
def compare_k(list_one,list_two):
    combination_num = (len(list_1) * (len(list_1) - 1)) / 2
    log_max_list = []
    i = 0
    for i in range(len(list_one)-1):#取出列表中的前n-1个元素，因为除了最后一个元素之外,其他都要作为分母
        denominator = list_one[i]#先取到列表中的第一个元素作为分母
        j = i + 1 #先取到分母之后的第一个元素作为分子，固定住i,i++的逻辑已经在for语句里面了
        while j < len(list_one):#当j不超过序列的长度时,打印值
            max_one = ((list_one[j]/list_one[i])/(list_two[j] / list_two[i])) if ((list_one[j]/list_one[i])/(list_two[j] / list_two[i])) > 1 else ((list_two[j]/list_two[i])/(list_one[j] / list_one[i]))
            j = j+1
            log_max_list.append(log(max_one))
            # print(log(max_one))

    # print(sum(log_max_list))
    # print(exp((sum(log_max_list))/combination_num)-1)#结果越接近0,说明两条曲线的相似度越高

    # plt.plot(list_1)
    # plt.plot(list_2)

    # plt.plot(list_1_log)
    # plt.plot(list_2_log)
    # plt.show()
    return(exp((sum(log_max_list))/combination_num)-1)


# compare_k(list_1,list_2)


######################################################################################################
for i in range(50000):
    list_1 = []
    price1 = 10
    list_1.append(price1)
    for i in range(40):
        zhangdie = 0.1 * random.uniform(-0.9, 1)
        price1 = price1 + price1 * zhangdie
        list_1.append(price1)
    list_1_log = [log(i) for i in list_1]
    list_2 = []
    price2 = 10.5
    list_2.append(price2)
    for j in range(40):
        zhangdie = 0.1 * random.uniform(-0.9, 1)
        price2 = price2 + price2 * zhangdie
        list_2.append(price2)
    list_2_log = [log(i) for i in list_2]
    s = compare_k(list_1,list_2)
    if s<0.07:
        print(s)
        plt.plot(list_1_log)
        plt.plot(list_2_log)
        plt.show()


# compare_k(list_1, list_3)

# print(db.collection_names())#打印表名
# posts = db.post
# # print(dir(posts))
# print(posts.count())
# for item in posts.find():
#     print(item)



