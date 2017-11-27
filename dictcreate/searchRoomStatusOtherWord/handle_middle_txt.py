#!/usr/bin python
# -*- coding:utf-8 -*-

import json
from utils import fileops
import jieba
import re
import pandas as pd

if __name__ == '__main__':
    dataPath = 'D:\workstation\\repositories\mayiPlayground\dictcreate\searchRoomStatusOtherWord\\'
    latentList = fileops.readListFromTxt(dataPath+'middle.txt')
    signalList = ['！','，','丶','~','➕',',','^','］','-','+','。','：','？','～','?','、',', ','‘','，',\
                  '[',' ','    ','…','…','(',')',']','（','）','.','=','～'\
                  '啊','么','咯','啦','的','哟','吗','哈','呀',
                  '了','诶','哦','吧','吧','啊','呵','喽','呦']

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
                if idx - 2 >= 0:
                    left2 = latentList[idx - 2]
                if idx - 1 >= 0:
                    left1 = latentList[idx - 1]
                if idx + 1 <= len(latentList):
                    right1 = latentList[idx + 1]
                if idx + 2 <= len(latentList):
                    right2 = latentList[idx + 2]
                # latentWordList.append([left2,left1,latentList[idx],right1,right2])

                rightSent = ''
                if not re.match('^\d*$',right1) and right1 not in signalList:
                        # if not re.match('^\d*$', right2) and right2 not in signalList:
                        #         rightSent = latentList[idx] + right1 + right2
                        #         if len(rightSent) >=6 and len(right2) >= 2:
                        #             rightSent = latentList[idx] + right1
                        # else:
                        #     rightSent = latentList[idx] + right1

                        rightSent = latentList[idx] + right1

                # rightSent = latentList[idx] + right1 + right2.replace(' ', '')
                # rightSent = re.sub('\d*', '', rightSent)
                # rightSent = rightSent.replace('！', '').replace('，', '').replace(',', '').replace('。', '') \
                #     .replace('？', '').replace('?', '').replace('、', '').replace('[', '') \
                #     .replace('，', '').replace('[', '')
                if rightSent:
                    latentWordList.append(rightSent)

    latentWordList = list(set(latentWordList))
    print(len(latentWordList))
    fileops.writeList2csv(dataPath+'latent_word_list.txt', latentWordList)