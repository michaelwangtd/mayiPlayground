#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops
import re
import time
from collections import OrderedDict

def getSplitSessionByTimestamp(sessionList):
    idx2sentenceDic = dict()
    timestamp2idxDic = dict()
    tsList = []
    tsymdList = []

    for line in sessionList:
        line = line.strip()
        if line:
            lineList = line.split(' ')
            i = lineList[:1][0]
            sentenceList = lineList[1:-2]
            timeList = lineList[-2:]
            timestamp = time.mktime(time.strptime(' '.join(timeList), '%Y-%m-%d %H:%M:%S'))
            # print(i,sentenceList,timeList,timestamp)

            # idx2sentenceDic[i] = sentenceList
            idx2sentenceDic[i] = line
            timestamp2idxDic[timestamp] = i
            tsList.append(timestamp)
            tsymdList.append(timeList[0])

    tsymdList = sorted(list(set(tsymdList)), reverse=True)
    tsymdList = [time.mktime(time.strptime(tsymd, '%Y-%m-%d')) for tsymd in tsymdList]
    # print(tsymdList)

    tsClassifyDic = OrderedDict()
    for tsymd in tsymdList:
        tsClassifyDic[tsymd] = []

    tsList = sorted(tsList)
    for ts in tsList:
        for k, v in tsClassifyDic.items():
            if ts > k:
                v.append(ts)
                break
    resultList = []
    resultStrList = []
    for k, v in tsClassifyDic.items():
        itemResultList = []
        itemResultStr = ''
        for ts in v:
            itemResultList.append(idx2sentenceDic[timestamp2idxDic[ts]])
            itemResultStr = itemResultStr + idx2sentenceDic[timestamp2idxDic[ts]] + '\n'
        resultList.append(itemResultList)
        resultStrList.append(itemResultStr)

    return resultList


if __name__ == '__main__':

    testSession = """0 tenant:您好，我们一行4人，过来旅游，想要预定11月19日-11月22日的房，共3天，请问这个时间方便接待吗? 2016-11-16 08:43:33
1 landlord:可以 2016-11-16 10:23:27
2 tenant:我需要跟你碰面吗 2016-11-16 11:32:20
3 landlord:不好意思房子已经被人订了！ 2016-11-16 11:34:15
4 tenant:啊 上面不是显示还有么 2016-11-16 11:34:40
5 tenant:下手慢了 2016-11-16 11:35:20
6 landlord:是的！刚下的订单！ 2016-11-16 11:35:43
7 tenant:如果那几天有人爽约了 请告诉我 2016-11-16 19:42:03
8 tenant:真的蛮喜欢你的房子的 2016-11-16 19:42:11
9 landlord:好 2016-11-16 19:42:48
10 tenant:住十天有折扣吗 2016-12-26 19:46:25
11 landlord:什么时候 2016-12-26 22:06:15
12 tenant:2号到12号 2016-12-26 22:24:00
13 landlord:你住几个人 2016-12-26 23:00:05
14 tenant:3个大人 一个11个月婴儿 2016-12-26 23:01:58
15 landlord:可以住的 2016-12-26 23:02:18
16 tenant:需要跟你碰面吗 2016-12-26 23:02:39
17 landlord:不需要，你可以先下单，不满意可以退了！ 2016-12-26 23:03:14
18 landlord:平台不允许见面， 2016-12-26 23:05:18
19 tenant:好了 2016-12-26 23:10:59
20 landlord:我确认了！谢谢！ 2016-12-26 23:11:19
21 tenant:新年快乐 你家地址哪里 怎么入住 2017-01-01 08:00:16
22 landlord:你是订的哪天 2017-01-01 18:37:24
23 landlord:你们是明天住吗？我地址发了 2017-01-01 18:41:22
24 tenant:你联系过我的 我明天入住 2017-01-01 18:51:18
25 landlord:好的 2017-01-01 19:01:16
26 tenant:在吗 2017-01-08 20:20:10
27 landlord:在 2017-01-08 20:44:27
"""
    sessionList = testSession.split('\n')

    ## 测试
    # dateSplitSessionList = getSplitSessionByTimestamp(sessionList)
    # for itemList in dateSplitSessionList:
    #     print('------------------')
    #     for item in itemList:
    #         print(item)


