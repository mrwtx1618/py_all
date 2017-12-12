#encoding:utf8
import numpy


ahead = 'HelloWorld'  # 全局变量
showList = []  # 全局变量


def printAhead():
    print ahead


def printOther():
    city = 'beijing'  # city是局部变量
    print city + ahead


def printList():
    #global showList  # global代表引用全局变量,没办法，不写的话，showList就成局部变量了，赞吧
    showList.append(1)
    showList.append(2)
    print showList

printAhead()
printOther()
printList()















