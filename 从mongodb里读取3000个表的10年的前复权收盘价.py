#encoding:utf8
#本程序想要实现从mongodb里面读取3000个表的数据,取出前复权价格,每30个交易日形成一条曲线

import pymongo

conn = pymongo.MongoClient('localhost',27017) #创建连接
db_1 = conn.stock_data_ten_years_original #连接原始数据库来获取数据
db_2 = conn.stock_data_ten_years_adjusted #连接一个新的数据库来装处理好的只有4个字段的表
COLLECTION_NAME_FOUR='adjusted_4'
# print((db.collection_names()))#返回了一个列表,长度是3165,元素是表名
# print(type(db))
# test_list = ['sh600000','sh600001','sh600002','sh600003','sh600004','sh600005','sh600006','sh600007']
collection_names_list = db_1.collection_names()
print(len(collection_names_list))
# for single_code in test_list:
#     # print(single_code)
#
#     posts = db['%s'%single_code] #循环一个数据库里面的所有的表,直接用sh.sh600001的形式无法完成目标,所以现在用db['sh600001']这样的形式
#     print(posts)
#     print(posts['0'].find('股票代码','sh600000'))
# posts = db.post
# # print(posts.find())
# # print(posts['_id'])
# result_dict_list = []
for single_code in collection_names_list:
    # print(single_code)
    collection = db_1['%s'%single_code]
    # print(collection)
# collection = db.sh600000#浦发银行
# print(dir(collection))
    for items in collection.find():
        result_dict = {}#定义一个新的字典来装4个字段的数据,分别是股票代码,股票名,日期列表,价格列表
        data_number = (len(items)-2)#这个数字是每一只股票里面的记录的条数,比如第一只股票sh600000浦发银行共有4046条记录.而items的长度是4046所以要减去2
        code = items['0']['股票代码']#取出股票代码
        stock_brief = items['0']['股票名称']
        print(code,stock_brief)
        forward_adjusted_price_list = []#前复权价列表
        the_date_list = []#日期列表
#         print(code,stock_brief)
        for i in range(data_number):
            i = str(i)#字典里面的取值是['4046']这种形式的,所以要把int转换成str类型
            forward_adjusted_price = (items[i]['前复权价'])
            forward_adjusted_price_list.append(forward_adjusted_price)
            the_date = items[i]['交易日期']
            the_date_list.append(the_date)
        # print(the_date_list)
        # print(forward_adjusted_price_list)
        print(len(the_date_list))
        print(len(forward_adjusted_price_list))
        result_dict['code'] = code
        result_dict['name'] = stock_brief
        result_dict['date'] = the_date_list
        result_dict['forward_adjusted_price'] = forward_adjusted_price_list
        # result_dict_list.append(result_dict)
        print(result_dict)

        db_2[single_code].update_one({},{'$set':result_dict},upsert=True)
print(result_dict_list)
    # print(items['4046']['前复权价'])#一共有4046条记录
    # print(data_number)
# print(posts.count())















































