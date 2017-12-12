#encoding:utf8

#本段程序想把原来的数据库的程序补充完整

import urllib.request #引入这个模块是想从大智慧里拿数据
import datetime
import time
import pymongo


conn = pymongo.MongoClient('localhost',27017) #创建连接
db_1 = conn.stock_data_ten_years_original #连接原始数据库来获取数据
db_2 = conn.stock_data_ten_years_adjusted_divided_by_2 #连接一个新的数据库来装处理好的只有4个字段的表,代码,股票名,日期,平均价格
COLLECTION_NAME_FOUR='adjusted_4'
collection_names_list = db_1.collection_names()#现在这一步得到的是各个股票的代码,但是股票代码是小写的,所以要转化一下
collection_names_list_upper = [name.upper() for name in collection_names_list]#改成大写的代码,可以被取到大智慧里面



today = datetime.datetime.now()
begin_time=str(today)[:10].replace('-','')

print(today)
print(begin_time)


def Token():#get token这个函数是用来获取token的
    url ='http://gw.yundzh.com/token/access?appid=dcdc435cc4aa11e587bf0242ac1101de&secret_key=InsQbm2rXG5z'#这里appid和secret_key是预先拿到的
    f = urllib.request.urlopen(url) #<class 'http.client.HTTPResponse'>
    f=f.read() #f是个bytes类型
    f=eval(f) #把bytes类型转换成了dict类型
    token=f['Data']['RepDataToken'][0]['token']#根据token的位置拿到token
    return token



#转换时间格式,把一个时间戳转换为yyyymmdd格式
def timetran(t):
    timestamp = t #t是一个时间戳,
    timearray = time.localtime(timestamp)
    the_time = time.strftime("%Y-%m-%d",timearray)
    return the_time




def request_data(url):#request url for data #取数据
    for count in range(1):
        try:
            url=url+Token()
            # print(url)
            response=urllib.request.urlopen(url)
            html=response.read()
            json_table=eval(html)
            data_json=json_table['Data']['JsonTbl']['data'][0][0]['data'][0][1]['data']
            data=[[timetran(x[0]),round((x[1]+x[2])/2,2)] for x in data_json]#这里timetran把原来的unix时间变成了标准时间
            print(name.lower(),len(data))
            # collection = db_1['%s' % name]
            # db_2[name.lower()].update({'code':'%s'%name.lower()},{'$push':{'date':{'$each':data[0]}}})



            for i in range(len(data)):
                # print(name.lower())
                db_2[name.lower()].update({'code': '%s' % name.lower()}, {'$addToSet': {'date':data[i][0]}})
                db_2[name.lower()].update({'code': '%s' % name.lower()}, {'$push': {'avg_price_divided_2_price':data[i][1]}})

                print(data)
            judge=judge_condition(data)
            if judge:
                return data
            else:
                return False
        except Exception as e:
            if count==9:
                print(e)
                return False
            else:
                continue
# token = Token()
# print(token)
for name in collection_names_list_upper:
    the_url='http://gw.yundzh.com/quote/kline?obj=%s&begin_time=20170119-154033-223-8&end_time=20170530-154033-223-8&field=ShiJian,KaiPanJia,ShouPanJia&period=1day&token='%name
    data=request_data(the_url)




collection_names_list = db_1.collection_names()
def add_data():
    for single_code in collection_names_list:
        print(single_code)
        collection = db_1['%s' % single_code]
add_data()
        # db_2[single_code].update({'code':'%s'%single_code},{ '$addToSet': { 'date': { '$each': [ 'sss', "electronics", "accessories" ] } } },upsert=True)
        # db_2[single_code].update({'code': '%s' % single_code},{'$addToSet': {'date': {'$each': [str for str in test_list]}}}, upsert=True)
        # db_2[single_code].update({'code': '%s' % single_code},{'$addToSet': {'date': {'$each': odd_list}}}, upsert=True)
        # db_2[single_code].update({'code': '%s' % single_code},{'$push': {'avg_price_divided_2_price': {'$each': [number for number in number_list]}}}, upsert=True)
        # db_2[single_code].update({'code': '%s' % single_code},{'$push': {'avg_price_divided_2_price': {'$each': letter_list}}}, upsert=True)

#对每一个list,都执行add_data这个函数
# for single_list in the_list_all:
#     odd_list,even_list,letter_list = deal_list(single_list)
#     add_data()