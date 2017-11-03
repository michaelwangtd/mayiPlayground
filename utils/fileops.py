#!/usr/bin python
# -*- coding:utf-8 -*-
import os
import codecs
import pickle


def readListFromTxt(filePath):
    resultList = []
    fr = codecs.open(filePath,'r',encoding='utf-8')
    while True:
        line = fr.readline()
        if line:
            resultList.append(line.strip())
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


def dumpPickle(filePath,cake):
    '''
    :param filePath:filedir/pickle.pkl
    :param cake: object
    '''
    fw = open(filePath,'wb')
    pickle.dump(cake,fw)
    fw.close()

def loadPickle(filePath):
    '''
    :param filePath:filedir/pickle.pkl
    :return:cake：object
    '''
    fr = open(filePath,'rb')
    cake = pickle.load(fr)
    fr.close()
    return cake

def checkdir(path):
   if os.path.exists(path) == False:
       os.makedirs(path)


