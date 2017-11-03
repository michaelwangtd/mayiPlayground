#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops

"""
    按照频率将词语归类
"""

if __name__ == '__main__':
    datas = fileops.readListFromTxt('../data/wordcount.csv')
    print('datas len:',len(datas))

    freqDic = dict()
    for data in datas:
        dataList = data.strip().split(',')
        if len(dataList) == 2:
            num = round(float(dataList[1]))
            word = dataList[0]

            if num not in freqDic:
                freqDic[num] = []
            freqDic[num].append(word)

    print('freqDic len:',len(freqDic))
    resultList = []
    for fre,wordList in freqDic.items():
        # print('频率:',fre,'出现的词列表长度：',len(wordList))
        print(str(fre)+','+str(len(wordList)))

        if len(wordList)<2260:
            outLine = str(fre)+','+str(len(wordList))+','+str(wordList)
        else:
            outLine = str(fre)+','+str(len(wordList))
        resultList.append(outLine+'\n')

    fileops.writeList2csv('../data/wordFreCount.csv',resultList)



