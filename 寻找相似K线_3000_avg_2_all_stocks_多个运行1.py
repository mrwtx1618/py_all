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
from matplotlib import font_manager#想在图片中输出中文,需要用到这个










####################################程序开始的时间#####################
begin_time = datetime.datetime.now()
print(begin_time)#程序开始的时间

zh_font = font_manager.FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)
conn = pymongo.MongoClient('localhost',27017)
db_adjusted = conn.stock_data_ten_years_adjusted_divided_by_2_new
db_list_3 = conn.stock_data_dict_3_elements



# #######################---首先要得到用户输入的股票的tail_list里面的价格,股票名,日期---###############################
def code_to_tail(code):
    collection = db_adjusted['%s' % code]  # 先连接用户输入的代码的这个表
    for items in collection.find():
        # print(items)
        stock_name = items['name']  # 取出这只股票的股票名
        list_one_all = [round(i, 2) for i in items['avg_price_divided_2_price']] #取出了所有的价格
        tail_list = list_one_all[-30:]  # 取最近的30个交易日的数据,这个list是用户输入的参数
        list_date_all = items['date']  # 取出了所有的日期
        tail_date_list = list_date_all[-30:] # 取出了最近的30个日期
        return tail_list, stock_name, tail_date_list



#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
tail_list,stock_name,tail_date_list = code_to_tail('sh600000')#得到了用户输入的股票的最近30个交易日的价格,股票名,最近的30个交易日的日期
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#
#
#
# #######################---下面这个函数用来返回所有的要与用户输入的list相比较的list---#################################
# ###定义一个大的list,这个大的list里面的元素是字典,每一个字典含有3个字段,分别是股票名,30个价格为一个周期的价格list,对应的30个日期组成的日期list
def list_30():#最终返回了这个大的list
    all_codes = db_adjusted.collection_names()#先取出所有的股票代码
    single_dict_list = []
    for single_code in all_codes:
        collection = db_adjusted['%s' % single_code]#连接每一张表
        for item in collection.find():
            name = item['name']#拿到股票名
            list_all_dates = item['date']#拿到所有的日期
            list_all_dates_without_tails_30 = list_all_dates[:-30]#把最近的30个日期去掉
            list_all_dates_without_tails_30_list = []  # 定义这个大的list来装分割好的由30个日期的list组成的小的list
            list_all_stocks = [round(i,2) for i in item['avg_price_divided_2_price']]#先得到所有股票的所有的价格,取两位小数
            list_all_stocks_without_tails_30 = list_all_stocks[:-30]#把每一只股票的最近的30个交易日的价格去掉,用这个列表用来拆分比较
            list_all_stocks_without_tails_30_list = []#定义这个大的list来装分割好的由30个价格的list组成的小的list
            i = -31
            while -i + 30 < len(list_all_stocks_without_tails_30):
                list_all_stocks_without_tails_30_list.append(list_all_stocks_without_tails_30[i:i + 30])
                list_all_dates_without_tails_30_list.append(list_all_dates_without_tails_30[i:i+30])
                i += -1
            single_dict = {}#定义一个空字典来装3个字段,股票名,股票价格,日期
            single_dict['name'] = name
            single_dict['price_list_of_list'] = list_all_stocks_without_tails_30_list
            single_dict['list_of_date'] = list_all_dates_without_tails_30_list
            single_dict_list.append(single_dict)
            print(name)

    return single_dict_list

single_dict_list_ = list_30() #这个函数在数据构造好以后可以暂时不执行
#
#
#
#
#
#
# ###################################---定义比较k线的函数---##############################################################
#
def compare_k(list_one,list_two):#list_one是用户输入的列表,list_two是与之要比较的列表
    log_max_list = []
    i = 0
    combination_num = (len(list_one) * (len(list_one) - 1)) / 2 #定义组合数
    for i in range(len(list_one)-1):#取出列表中的前n-1个元素，因为除了最后一个元素之外,其他都要作为分母
        j = i + 1 #先取到分母之后的第一个元素作为分子，固定住i,i++的逻辑已经在for语句里面了
        while j < len(list_one):#当j不超过序列的长度时,打印值
            max_one = ((list_one[j]/list_one[i])/(list_two[j] / list_two[i])) if ((list_one[j]/list_one[i])/(list_two[j] / list_two[i])) > 1 else ((list_two[j]/list_two[i])/(list_one[j] / list_one[i]))
            j = j+3
            log_max_list.append(log(max_one))
    return(exp((sum(log_max_list))/combination_num)-1)





##################################从数据库stock_data_dict_3_elements里读数据#############################################
all_share_codes = db_list_3.collection_names()
# all_share_codes = ['sh600666','sh600111','sz300576','sh600005','sh600006','sh600007','sh600008','sh600009','sh600010','sh600011','sh600015','sh600016','sh600017','sh600018','sh600019','sh600020','sh600021','sh600022','sh600023']
# print(all_share_codes)
s_list_each_stock_all = []
# count = 0
for single_share in all_share_codes:
    the_collection = db_list_3['%s' % single_share]#连接每一张表
    s_list_each_stock = []
    for item in the_collection.find():
        name = item['name']#拿到股票名
        print(name)
        if item['price_list_of_list'] == []:
            # print('%s 数据不足！！'%name)
            continue
        else:
            temp_single_list_300 = []
            for single_list in item['price_list_of_list']:
                single_list_300 = item['price_list_of_list'][:1000]#定义一个新的List来装这些single_list_300
            for i in range(len(single_list_300)):
                s = compare_k(tail_list, (item['price_list_of_list'][i]))*100
                # print(s)
                s_list_each_stock.append(s)#每一只股票的s列表
            # count+=1
            # percent = round(((count/3165)*100),2)
            # print('complete percent:'+str(percent)+'%')
    s_list_each_stock_all.append(s_list_each_stock)
# print(s_list_each_stock_all)#3165只股票里面每一个的s值,现在的取法是每一只都取500个最近的交易日,所以这是一个大的list,里面的元素是3165个小的list,每一个list里面有500个s值






#####################################下面这一段是来找所有的3165*500个s值里面的3个最小值#####################################

def find_smallest_three():
    smallest_listed_all = []
    for single_s_list in s_list_each_stock_all:
        if single_s_list == []:
            print('%sS列表为空！！！！！！！！'%single_s_list)
            continue
        else:
            single_s_list_sorted = np.sort(single_s_list)
            # print(single_s_list)
            single_smallest = single_s_list_sorted[0]
            smallest_listed_all.append(single_smallest)
    smallest_listed_all_sorted = np.sort(smallest_listed_all)
    the_min_1 = smallest_listed_all_sorted[0]
    return the_min_1
the_min_1 = find_smallest_three()

# print('The smallest is',find_smallest_three())
# print(find_smallest_three())


#############下面这一段是来寻找最小值的位置,即寻找这个最小值出现在上面那个大的list里面的哪个小的List里面的第几个元素

def find_the_position(small):
    for single_list_ in s_list_each_stock_all:
        for value in single_list_:
            # print(value)
            if value == small:
                print(small)
                list_position = (s_list_each_stock_all.index(single_list_))
                element_position = (single_list_.index(small))
                return list_position,element_position






#########暂时返回的两个值是7和96,说明collection是第10个,k线是第197个,现在要从数据库里得到这条线##############
#这个函数的目标是返回两个list,一个是价格list,一个是这个价格list对应的日期,还有对应的股票名
#首先要根据数字9来确定collection_name
def return_2_list(the_collection_number,the_element_number):
    the_collection_code = all_share_codes[the_collection_number]
    the_collection_2 = db_list_3['%s' % the_collection_code]
    for item in the_collection_2.find():
        name_need = item['name']
        price_list = item['price_list_of_list']
        list_need = price_list[the_element_number]
        date_list = item['list_of_date']
        date_need = date_list[the_element_number]
        return name_need,list_need,date_need






def make_picture():
    fig1 = plt.figure(figsize=(10,8))#先创建第一幅图,构想为这幅图分为两部分,subplot(2,1,1)为最近30天的K线,subplot(2,1,2)为相似的K线，figsize来设置
    ax_up = fig1.add_subplot(2,1,1)#先做两幅图之间的上面的那幅图
    tail_date_datetime_list = [datetime.datetime.strptime(single_dates,'%Y-%m-%d') for single_dates in tail_date_list]
    ax_up.plot(tail_date_datetime_list,tail_list)#先做用户选定的那条K线,传入日期以及价格
    plt.xlabel('%s'%stock_name,fontproperties=zh_font)

    ax_down = fig1.add_subplot(2,1,2)#再做两幅图之间的下面的那幅图
    date_need_convert = [datetime.datetime.strptime(single_dates2, '%Y-%m-%d') for single_dates2 in date_need]
    ax_down.plot(date_need_convert,list_need)
    plt.xlabel('%s' % name_need, fontproperties=zh_font)
        # plt.plot(tail_list)
        # plt.plot(list_without_tail_list[i])
    plt.show()





which_collection_number,which_element_number = find_the_position(the_min_1)
print(which_collection_number,which_element_number)#打印出需要的collection在整个collection_list里面的序号,并且打印出是哪一个元素
name_need,list_need,date_need = return_2_list(which_collection_number,which_element_number)
print(name_need,list_need,date_need_convert)#name_need是哪一只股票,list_need是需要的价格列表

end_time = datetime.datetime.now()
print(end_time) #程序结束的时间
print(end_time-begin_time) #时间差





make_picture()#作图


#####################################程序结束的时间######################################



def show_users(code):#这个函数实现我输入一个代码,返回给我3只最像的3条K线
    pass















































































































