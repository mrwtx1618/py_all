#encoding:utf-8

import pymongo

conn = pymongo.MongoClient('localhost',27017) #创建连接
db_1 = conn.stock_data_ten_years_original #连接原始数据库来获取数据
db_2 = conn.stock_data_ten_years_adjusted_divided_by_2 #连接一个新的数据库来装处理好的只有4个字段的表,代码,股票名,日期,平均价格

the_list_1 = [[1,2,'a'],[3,4,'b'],[5,6,'c'],[7,8,'d'],[9,10,'e'],[11,12,'f'],[13,14,'g'],[15,16,'h'],[17,18,'i'],[19,20,'j']]
the_list_2 = [[7,8,'d'],[9,10,'e'],[11,12,'f'],[13,14,'g'],[15,16,'h'],[17,18,'i'],[19,20,'j']]
the_list_3 = [[1,2,'a'],[3,4,'b'],[5,6,'c'],[7,8,'d']]
the_list_all = [the_list_1,the_list_2,the_list_3]
# print(the_list_all)

odd_list_1 = []
even_list_1 = []
letter_list_1 = []

for element in the_list_1:
    odd_list_1.append(element[0])
    even_list_1.append(element[1])
    letter_list_1.append(element[2])

print(odd_list_1)
print(even_list_1)
print(letter_list_1)


# def deal_list(list_input):
#     odd_list = []
#     even_list = []
#     letter_list = []
#     for single_list in the_list_all:
#         list_input = single_list
#     for element in list_input:
#         odd_list.append(element[0])
#         even_list.append(element[1])
#         letter_list.append(element[2])
#     return odd_list,even_list,letter_list
#
# odd_list,even_list,letter_list = deal_list(the_list_all)
# print(odd_list)
# print(even_list)
# print(letter_list)
# print(list_all)

###希望写一个处理每一个小的list的函数,然后对大的list进行循环

def deal_list(small_list):
    odd_list = []
    even_list = []
    letter_list = []
    for element in small_list:
        odd_list.append(element[0])
        even_list.append(element[1])
        letter_list.append(element[2])
    return odd_list,even_list,letter_list





# for single_list in the_list_all:
#     odd_list,even_list,letter_list = deal_list(single_list)
# print(odd_list,letter_list)



# collection_names_list = db_1.collection_names()
# def add_data():
#     for single_code in collection_names_list:
#         # print(single_code)
#         collection = db_1['%s' % single_code]
#
#         db_2[single_code].update({'code':'%s'%single_code},{ '$addToSet': { 'date': { '$each': [ 'sss', "electronics", "accessories" ] } } },upsert=True)
#         # db_2[single_code].update({'code': '%s' % single_code},{'$addToSet': {'date': {'$each': [str for str in test_list]}}}, upsert=True)
#         db_2[single_code].update({'code': '%s' % single_code},{'$addToSet': {'date': {'$each': odd_list}}}, upsert=True)
#         # db_2[single_code].update({'code': '%s' % single_code},{'$push': {'avg_price_divided_2_price': {'$each': [number for number in number_list]}}}, upsert=True)
#         db_2[single_code].update({'code': '%s' % single_code},{'$push': {'avg_price_divided_2_price': {'$each': letter_list}}}, upsert=True)
#
# #对每一个list,都执行add_data这个函数
# for single_list in the_list_all:
#     odd_list,even_list,letter_list = deal_list(single_list)
#     add_data()














