#!/usr/bin python
# -*- coding:utf-8 -*-

import os
from utils import fileops
import jieba

if __name__ == '__main__':
    dataDir = '../data/mayiserver'
    fileList = ['tenant_chat_01.csv','tenant_chat_02.csv']

    jieba.load_userdict(dataDir+'/dic.txt')
    targetList = fileops.readListFromTxt(dataDir+'/feature_word_question_thick.txt')
    # targetList = fileops.readListFromTxt(dataDir+'/feature_word_question_dic.txt')
    # targetList = fileops.readListFromTxt(dataDir+'/feature_word_question_thin.txt')

    tenantidList = []
    tenantRoomStatusList = []
    notRoomStatusList = []
    i = 1
    for fname in fileList:
        fpath = os.path.join(dataDir,fname)

        datas = fileops.readListFromTxt(fpath)

        for line in datas:
            lineList = line.replace('\r', '').replace('\n', '').strip().split(',')
            if len(lineList) == 2:
                tenantId = lineList[0]
                content = lineList[1]
                cutWordList = list(jieba.cut(content))

                tenantidList.append(tenantId)

                interList = list(set(cutWordList).intersection(set(targetList)))
                if interList:
                    tenantRoomStatusList.append(tenantId)
                else:
                    notRoomStatusList.append(line)

                # for word in cutWordList:
                #     if word in targetList:
                #         tenantRoomStatusList.append(tenantId)
                #         break

                i = i + 1
                # if i>1000:
                #     break
                print(i)
        print('tenantidList：',len(tenantidList),len(list(set(tenantidList))))
        print('tenantRoomStatusList：',len(tenantRoomStatusList),len(list(set(tenantRoomStatusList))))
        print('notRoomStatusList：',len(notRoomStatusList),len(list(set(notRoomStatusList))))

        outPath = 'D:\workstation\\repositories\mayiPlayground\data\mayiserver\output\\noRoomStatusList.txt'
        fileops.writeList2csv(outPath,list(set(notRoomStatusList)))
        exit(0)

    # print('tenantidList：', len(tenantidList), len(list(set(tenantidList))))
    # print('tenantRoomStatusList：', len(tenantRoomStatusList), len(list(set(tenantRoomStatusList))))
