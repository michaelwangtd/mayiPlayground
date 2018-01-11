#!/usr/bin python
# -*- coding:utf-8 -*-

import pandas as pd
import jieba
from collections import OrderedDict
import os

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


if __name__ == '__main__':
    root_path = 'D:/data/cache'
    fnames = ['1_图.txt','2_钱.txt','3_床.txt','4_地址.txt']

    dic = OrderedDict()
    tags = []
    lines = []
    for f in fnames:
        tag = f.strip().split('.')[0].split('_')[-1]
        fpath = os.path.join(root_path,f)
        line_list = readListfromTxt(fpath)

        for line in line_list:
            dic[tag] = line
            tags.append(tag)
            lines.append(line)
    writeList2csv(root_path+'/input.txt',lines)
    writeList2csv(root_path+'/label.txt',tags)