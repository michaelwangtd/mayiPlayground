#!/usr/bin python
# -*- coding:utf-8 -*-

import codecs

class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls._instence):
            cls._instence = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instence



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

def writeList2csv(filePath,infoList):
    fw = open(filePath,'w',encoding='utf-8')
    for itemList in infoList:
        line = ''
        if isinstance(itemList,list):
            line = ','.join(itemList)
        if isinstance(itemList,str):
            line = itemList.strip()
        if line:
            fw.write(line + '\n')
    fw.close()

def getItemSetList(infos):
    result_list = []
    for info in infos:
        result_list.append(' '.join(sorted(list(set(info.split(' '))),key=lambda item:len(item))))
    return result_list


if __name__ == '__main__':
    infos = readListfromTxt('d:/data/input.txt')
    # infos = getItemSetList(infos)
    print(len(infos))
    infos = list(set(infos))
    print(len(infos))
    result = sorted(infos)
    writeList2csv('d:/data/result.txt',result)

    # 1
    # for item in result:
    #     print(item)

    # 2
    out = []
    for item in result:
        out.extend(item.strip().split(' '))
    for item in out:
        print(item)
