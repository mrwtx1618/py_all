#encoding:utf8

import pandas as pd
import pymongo
import json
import os

conn = pymongo.MongoClient('localhost',27017)
db = conn.stock_data_ten_years_original
code_list = os.listdir('F:\BaiduNetdiskDownload\stock_yhj\stock')

for filename in code_list:
    collection_name = '%s'%filename[:-4]
    df = pd.read_csv('F:\BaiduNetdiskDownload\stock_yhj\stock\%s'%filename,encoding='gbk')
    code = df['股票代码'][0]
    name = df['股票名称'][0]
    print(code,name)
    records = json.loads(df.T.to_json())
    db[collection_name].update({},{'$set':records},upsert = True)



















