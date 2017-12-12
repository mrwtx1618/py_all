#encoding:utf8
#break的用法,跳出整个for循环
#运行的结果是只打印了0,1,2,3,4
for i in range(10):
    if i==5:
        break
    print(i)
print('\n')#打印空行
print('\n')
#continue的用法,跳出本次循环,接着下次继续
#只是不打印5
for j in range(10):
    if j==5:
        continue
    print(j)


















