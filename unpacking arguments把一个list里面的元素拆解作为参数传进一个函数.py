#encoding:utf-8
def health_calculator(age,apples_ate,cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)
my_answer = [27,20,0]
health_calculator(*my_answer)#用一个*号可以把一个list的3个元素作为变量传入作为函数参数












