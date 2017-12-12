#encoding:utf-8
#尝试连接一个远程的数据库


import pymongo
import datetime


today = str(datetime.date.today()-datetime.timedelta(days=1))
# print(today)
conn = pymongo.MongoClient('116.226.242.109',27017)
db = conn.all_result_test
collection = db[today]
for items in collection.find():
    print(items)











