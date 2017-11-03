#!/usr/bin python
# -*- coding:utf-8 -*-

import os
from utils import fileops

if __name__ == '__main__':

    fileDir = 'd:/data/simplechat/simplechat2/'
    fnameList = os.listdir(fileDir)
    print('file name length:', len(fnameList))

    fnameLenDic = dict()
    for i in range(len(fnameList)):
        fname = fnameList[i]
        filePath = os.path.join(fileDir,fname)
        chatList = fileops.readListFromTxt(filePath)
        fnameLenDic[fname] = len(chatList)

        if len(chatList) >= 4 and len(chatList) <= 10:
            for line in chatList:
                print(line)
            print('----------------------')
    # exit(0)

        # print(i)
        # if i>1000:
        #     break

    lengthFileNameDic = dict()
    for fname,chatLength in fnameLenDic.items():
        if chatLength not in lengthFileNameDic:
            lengthFileNameDic[chatLength] = []
        lengthFileNameDic[chatLength].append(fname)

    chatLenAndFileNumList = []
    for k,v in lengthFileNameDic.items():
        chatLenAndFileNumList.append([k,len(v)])

    fileops.dumpPickle('../pickle/chatLen.pkl',chatLenAndFileNumList)
