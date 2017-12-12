#encoding:utf-8
#两种list的转换方法
#1.有两个list,一个List的值是keys,另一个list的值是values,现在想把这两个list合并成一个dict
the_key_list = ['key1','key2','key3']
the_value_list = [['value1'],['value4','value5','value6'],['value7','value8','value9'],['value10','value11']]








print(the_value_list.index(['value1']))



the_dict = dict(zip(the_key_list,the_value_list))
print(list(the_dict.keys())[0])


# for i in range(len(the_key_list)):
#     print(the_dict['%s'%the_key_list[i]])
# print(the_dict['key1'])





# print(list(the_dict.items()))













