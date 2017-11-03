#!/usr/bin python
# -*- coding:utf-8 -*-

import os
from utils import fileops
import re

if __name__ == '__main__':

    fileDir = 'd:/data/simplechat/simplechat2/'
    fnameList = os.listdir(fileDir)
    print('file name length:', len(fnameList))

    for i in range(len(fnameList)):
        fname = fnameList[i]
        filePath = os.path.join(fileDir,fname)
        chatList = fileops.readListFromTxt(filePath)

        chatStr = '\n'.join(chatList)

        # # if '这套' in chatStr:
        # # if re.findall('(号)',chatStr,re.S):
        # if re.findall('(\d+号.*(有|没有).*号.*(有|没有))',chatStr,re.S):
        #     reList = re.findall('(号.*号)',chatStr,re.S)
        #     # if len(reList)>3:
        #     if reList:
        #         print('----------------------')
        #         print(reList)
        #         for line in chatList:
        #             print(line)

        flage = False
        for chat in chatList:
            if re.findall('(\d+号.*(有|没有).*号.*(有|没有))',chat,re.S):
                flage = True
                break
        if flage:
            print('-------------')
            for line in chatList:
                print(line)