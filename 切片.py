#encoding:utf8
my_list = [1,2,3,4,5,6,7,8,9,10]

print my_list[0:3] #取list的前三个元素
print my_list[1:-1] #打印列表里面的第二个元素到倒数第二个元素
print my_list[1:] #打印第二个元素一直到最后一个元素
print my_list[-1] #打印倒数第一个元素
print my_list[-1:] #打印倒数第一个元素返回的列表
print my_list[-3:] #打印倒数第三个元素

#切片操作十分有用。我们先创建一个0-99的数列
L = list(range(100))
print L

#可以通过切片操作轻松取出某一段数列,比如前10个数字
print L[:10] #打印前10个数,前面那个冒号没写数字，则默认为0
print L[-10:] #打印倒数10个数字
print L[:-10] #打印第一个到第倒数10个数字
print L[10:20] #打印第11至第20个数字
print L[:] #打印所有的数字，因为冒号前后都省略了，则默认从0取到最后一个数字
print L[::5] #打印所有的数字,，每5个数字取一个。
print L[:10:2] #前10个数字每两个取一个

#对字符也可以进行切片
my_str = 'ABCDFGHIJKLMN'
print my_str[::2]













