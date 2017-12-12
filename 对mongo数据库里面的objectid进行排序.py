#encoding:utf8

import pymongo
import datetime


conn = pymongo.MongoClient('localhost',27017)
db = conn.similar_result
the_stock_list = db.collection_names()
the_datetime_list = []
for code in the_stock_list:
    the_collection = db['%s'%code]
    # print(int((str(the_collection.find_one()['_id'])[:8]),16))#把16进制的字符串转换成10进制的数字
    the_datetime = datetime.datetime.fromtimestamp(int((str(the_collection.find_one()['_id'])[:8]),16))
    the_datetime_list.append(the_datetime)
    print(type(the_datetime))
print(sorted(the_datetime_list,reverse = True))
















