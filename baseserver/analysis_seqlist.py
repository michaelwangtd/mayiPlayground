#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops
import pandas as pd

if __name__ == '__main__':
    datas = pd.read_csv('D:/data/2017-03.csv')
    seqListCol = datas['3_seqlist']
    # print(type(seqListCol),len(seqListCol))
    lineList = []
    for item in list(seqListCol):
        if isinstance(item,str):
            if item.strip():
                lineList.append(item)
    print(type(lineList),len(lineList))
