#!/usr/bin python
# -*- coding:utf-8 -*-

import jieba
import pandas as pd
import random

jieba.load_userdict('./usrdic.txt')
tag_dic = {'地址':'t_addr','押金':'t_mony','空调':'t_airc','钥匙':'t_key'}
tag_word_list = ['地址','押金','空调','钥匙']

def readListfromTxt(filePath):
    resultList = []
    fr = open(filePath, 'r', encoding='utf-8')
    while True:
        line = fr.readline()
        if line:
            line = line.strip()
            if line:
                resultList.append(line)
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
            line = itemList
        if line:
            fw.write(line + '\n')
    fw.close()

if __name__ == '__main__':
    lines = readListfromTxt('./seed_sentence.txt')
    random.shuffle(lines)

    out_list = []

    for line in lines:
        item_tag_list = []
        line = str(line)
        cut_words = list(jieba.cut(line))

        for word in cut_words:
            w_and_t = ''
            if word in tag_word_list:
                w_and_t = word + '  ' + tag_dic[word]
            else:
                w_and_t = word + '  ' + 'O'
            if w_and_t:
                item_tag_list.append(w_and_t)

        item_line = '\n'.join(item_tag_list)+'\n'
        out_list.append(item_line)

    writeList2csv('./data.txt',out_list)


