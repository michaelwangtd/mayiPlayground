#!/usr/bin python
# -*- coding:utf-8 -*-

import os
from utils import fileops
import jieba

if __name__ == '__main__':
    dataDir = 'D:\\workstation\\repositories\\mayiPlayground\\data\\mayiserver'
    fileList = ['tenant_chat_01.csv','tenant_chat_02.csv']

    jieba.load_userdict(dataDir+'/dic.txt')
    # targetList = fileops.readListFromTxt(dataDir+'/feature_word_question_thick.txt')
    targetList = fileops.readListFromTxt(dataDir+'/feature_word_question_dic.txt')
    # targetList = fileops.readListFromTxt(dataDir+'/feature_word_question_thin.txt')

    classifyDic = dict()
    classifiedCountDic = dict()
    door = 1

    # i = 1
    # # 1
    # for fname in fileList:
    #     fpath = os.path.join(dataDir, fname)
    #
    #     datas = fileops.readListFromTxt(fpath)
    #
    #     for line in datas:
    #         lineList = line.replace('\r', '').replace('\n', '').strip().split(',')
    #         if len(lineList) == 2:
    #             tenantId = lineList[0]
    #             content = lineList[1]
    #
    #             if tenantId not in classifyDic:
    #                 classifyDic[tenantId] = []
    #             classifyDic[tenantId].append(content)
    #             i += 1
    #             print(i)
    #     # break
    # print('-----------1--------')
    # fileops.dumpPickle(dataDir + '/classifyDic.pkl', classifyDic)
    #
    #
    # # 2
    # for tId,chatList in classifyDic.items():
    #     chatNum = len(chatList)
    #     chatRoomNum = 0
    #
    #     for chat in chatList:
    #         cutWordList = list(jieba.cut(chat))
    #         interList = list(set(cutWordList).intersection(set(targetList)))
    #         if interList:
    #             chatRoomNum += 1
    #
    #     rate = float(chatRoomNum/chatNum)
    #
    #     classifiedCountDic[tId] = [chatNum,chatRoomNum,rate]
    # print('-----------2-------------')
    #
    # fileops.dumpPickle(dataDir + '/classifiedCountDic.pkl',classifiedCountDic)

    classifyDic = fileops.loadPickle(dataDir + '/classifyDic.pkl')
    classifiedCountDic = fileops.loadPickle(dataDir + '/classifiedCountDic.pkl')

    # 3
    totalTenantIdList = []
    roomStatAndOtherInfoIdList = []
    onlyRoomStatIdList = []
    noRoomStatIdList = []
    for tId,numList in classifiedCountDic.items():
        totalTenantIdList.append(tId)

        if len(numList) == 3:
            if numList[2] < float(door) and numList[2] > float(0):
                roomStatAndOtherInfoIdList.append(tId)
            if numList[2] <= float(0):
                noRoomStatIdList.append(tId)
            if numList[2] >= float(door):
                onlyRoomStatIdList.append(tId)

    totalTenantIdList = list(set(totalTenantIdList))
    roomStatAndOtherInfoIdList = list(set(roomStatAndOtherInfoIdList))
    onlyRoomStatIdList = list(set(onlyRoomStatIdList))
    noRoomStatIdList = list(set(noRoomStatIdList))

    print('totalTenantIdList',len(totalTenantIdList))
    print('roomStatAndOtherInfoIdList',len(roomStatAndOtherInfoIdList))
    print('onlyRoomStatIdList',len(onlyRoomStatIdList))
    print('noRoomStatIdList',len(noRoomStatIdList))
    print('roomStatAndOtherInfoIdList/totalTenantIdList',len(roomStatAndOtherInfoIdList)/len(totalTenantIdList))

