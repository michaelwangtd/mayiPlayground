#!/usr/bin python
# -*- coding:utf-8 -*-

import codecs

"""
    获取差集
"""


def readListfromTxt(filePath):
    resultList = []
    fr = codecs.open(filePath,'r',encoding='utf-8')
    while True:
        line = fr.readline()
        if line:
            line = line.strip()
            if line:
                resultList.append(line)
        else:
            break
    fr.close()
    return resultList


def writeList2csv(filePath,infoList):
    fw = codecs.open(filePath,'w',encoding='utf-8')
    for itemList in infoList:
        line = ''
        if isinstance(itemList,list):
            line = ','.join(itemList)
        if isinstance(itemList,str):
            line = itemList.strip()
        if line:
            fw.write(line + '\n')
    fw.close()


if __name__ == '__main__':
    A = readListfromTxt('d:/data/input.txt')
    B = readListfromTxt('d:/data/result.txt')
    print('A：',len(A))
    print('B：',len(B))
    print('A-B：',len(A)-len(B))

    re = list(set(A).difference(set(B)))  # A中有而B中没有的

    print('re',len(re))
    result = sorted(re)
    writeList2csv('d:/data/result.txt',result)
