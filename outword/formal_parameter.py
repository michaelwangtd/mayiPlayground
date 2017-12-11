#!/usr/bin python
# -*- coding:utf-8 -*-

def outputNum(a1,a2,a3):
    print(a1,a2,a3)

def outputNum2(a,*args):
    print('a1:',a)
    print('args:',type(args),args)
    for arg in args:
        for item in arg:
            print(item)

def outputNum3(a,b,c):
    print(a,b,c)


if __name__ == '__main__':
    # 1
    # tList = [1,2,3]
    # outputNum(*tList)   # 1 2 3
    # # 2
    # a1 = 1
    # tList2 = [1,2,3,4]
    # outputNum2(a1,tList2)   # a1: 1 # args: <class 'tuple'> ([1, 2, 3, 4],)
    # 3
    a2 = 2
    dic = {'b':'b','c':'c'}
    outputNum3(a2,**dic)
