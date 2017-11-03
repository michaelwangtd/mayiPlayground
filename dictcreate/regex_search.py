#!/usr/bin python
# -*- coding:utf-8 -*-

import re

def readListfromTxt(filePath):
    resultList = []
    fr = open(filePath,'r',encoding='utf-8')
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

if __name__ == '__main__':

    resultList = []

    infos = readListfromTxt('d:/data/input.txt')

    for line in infos:
        if re.match('(\d*月\d*日)',line,re.S):
            res = re.match('(\d*月\d*日)',line,re.S).group(0)
            res = res.replace('日','号')
            print(res)
