#!/usr/bin python
# -*- coding:utf-8 -*-

import codecs

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
    infos = readListfromTxt('d:/data/input.txt')
    print(len(infos))
    infos = list(set(infos))
    print(len(infos))
    result = sorted(infos)
    writeList2csv('d:/data/result.txt',result)
