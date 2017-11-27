#!/usr/bin python
# -*- coding:utf-8 -*-

import json
from utils import fileops
import jieba
import re
import pandas as pd

if __name__ == '__main__':
    dataPath = 'D:\workstation\\repositories\mayiPlayground\dictcreate\searchRoomStatusOtherWord\\'
    userdicList = fileops.readListFromTxt(dataPath+'userdic.txt')
    jieba.load_userdict(dataPath+'userdic.txt')

    lineList = []

    infos = pd.read_csv('D:/data/corpus/2017-02.csv')
    datas = infos['4_cutlistrow']
    tempData = []
    for data in datas:
        if isinstance(data,str):
            if data.strip():
                tempData.append(data.strip())
    datas = tempData
    print(len(datas),type(datas))

    for data in datas:
        lineList.extend(data.split('\n'))

    print('linelist:',len(lineList))

    latentList = []
    for line in lineList:
        if '没有' in line:
            cutWordList = list(jieba.cut(line))
            insertSectionList = list(set(cutWordList).intersection(set(userdicList)))
            if not insertSectionList:
                latentList.append(line)
    print('latentList:',len(latentList))
    latentList = list(set(latentList))
    fileops.writeList2csv(dataPath+'middle.txt',latentList)