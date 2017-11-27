#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops

if __name__ == '__main__':
    datas = fileops.readListFromTxt('D:/data/2017-03.csv')
    print(len(datas))

    part1 = datas[:int(len(datas)/4*1)]
    part2 = datas[int(len(datas)/4*1):int(len(datas)/4*2)]
    part3 = datas[int(len(datas)/4*2):int(len(datas)/4*3)]
    part4 = datas[int(len(datas)/4*3):]

    fileDir = 'D:/data/2017-03-'
    fileops.writeList2csv(fileDir+'part1.csv',part1)
    fileops.writeList2csv(fileDir+'part2.csv',part2)
    fileops.writeList2csv(fileDir+'part3.csv',part3)
    fileops.writeList2csv(fileDir+'part4.csv',part4)