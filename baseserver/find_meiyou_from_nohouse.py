#!/usr/bin python
# -*- coding:utf-8 -*-

import json
from utils import fileops
import jieba
import re

if __name__ == '__main__':
    failList = ['没有了','没有了','没有任何','没有哟',
                '没有房','没有房子','没有房间','没有的','没有房间']

    datas = json.load(open('d:/data/no_house.json','r',encoding='utf-8'))
    print(type(datas),len(datas))

    rawList = []
    for k,v in datas.items():
        contentDic = v['4_cutlistrow']
        if len(contentDic)>=1:
            if contentDic['0']!=None:
                oriCor = contentDic['0']
                oriCorList = oriCor.split('\n')
                if oriCorList:
                    rawList.append(oriCorList)

    latentList = []
    for rawItemList in rawList:
        for raw in rawItemList:
            if '没有' in raw:
                for word in failList:
                    if not word in raw:
                        latentList.append(raw)
    latentList = list(set(latentList))
    print('latentList：',len(latentList))

    latentWordList = []
    for latent in latentList:
        left2 = ''
        left1 = ''
        right1 = ''
        right2 = ''
        latentList = list(jieba.cut(latent))
        if '没有' in latentList:
            if latentList.index('没有'):
                idx = latentList.index('没有')
                if idx-2 >= 0:
                    left2 = latentList[idx-2]
                if idx-1 >= 0:
                    left1 = latentList[idx-1]
                if idx+1 <= len(latentList):
                    right1 = latentList[idx+1]
                if idx+2 <= len(latentList):
                    right2 = latentList[idx+2]
                # latentWordList.append([left2,left1,latentList[idx],right1,right2])

                rightSent = latentList[idx]+right1+right2.replace(' ','')
                rightSent = re.sub('\d*','',rightSent)
                rightSent = rightSent.replace('！','').replace('，','').replace(',','').replace('。','') \
                    .replace('？', '').replace('?','').replace('、','').replace('[','')\
                    .replace('，','').replace('[','')
                latentWordList.append(rightSent)

    latentWordList = list(set(latentWordList))
    print(len(latentWordList))
    fileops.writeList2csv('D:/data/meiyou_latent.txt',latentWordList)