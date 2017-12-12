#encoding:utf8

#现在想把3000多个csv存到数据库里面，直接使用mongoimport命令似乎无法批量导入,现在换用python来导入
#想法是先用pandas模块把csv读入到内存里面,然后用pymongo模块里面的update_one命令存入到数据库里面


import pandas as pd
import pymongo
import json
conn = pymongo.MongoClient('localhost',27017)
db = conn.stock_data_ten_years_original
COLLECTION_600000='sh600000'



df = pd.read_csv('F:/BaiduNetdiskDownload/stock_yhj/stock/sh600000.csv',encoding='gbk')
print(type(df))
# code = df['股票代码'][0]
# name = df['股票名称'][0]
# print(code,name)
# dict1 = (df.to_json())
dict1 = json.loads(df)
print(type(dict1))
# print(dict_)
# # print(dict_)
db[COLLECTION_600000].update({},{'$set':dict1},upsert=True)














