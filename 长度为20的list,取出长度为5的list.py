#encoding:utf8
list_1 = [i for i in range(20)]
print(list_1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(len(list_1))
#现在想实现的功能是最后的15,16,17,18,19这样的5个元素不要,而从14开始倒数,每5个元素形成一个小的list
without_tail_list = list_1[:-5]
tail_list = list_1[-5:]
print(tail_list)
print(without_tail_list)
i = -6
while -i+5<=len(list_1):
    print(without_tail_list[i:i+5])
    i+=-1
# print(without_tail_list[-5:])
# print(without_tail_list[-6:-1])
# print(without_tail_list[-7:-2])
# print(without_tail_list[-8:-3])
# print(without_tail_list[-9:-4])
# print(without_tail_list[-10:-5])
# print(without_tail_list[-11:-6])
# print(without_tail_list[-12:-7])
# print(without_tail_list[-13:-8])
# print(without_tail_list[-14:-9])
# print(without_tail_list[-15:-10])
# print(without_tail_list[-16:-11])
# print(without_tail_list[-17:-12])




















