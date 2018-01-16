#!/usr/bin python
# -*- coding:utf-8 -*-

import pandas as pd
import csv
import gensim
from gensim.models.keyedvectors import KeyedVectors

"""
    model type trans to model.txt
"""

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

if __name__ == '__main__':
    # df = pd.read_csv('../data/glove.6B.100d.txt',header=None,\
    #                  sep=' ',quoting=csv.QUOTE_NONE)
    # print(df.head(5))
    # print(df.describe())

    fp = 'D:\\resource_collection\\nlp\\word2vec_model\\word2vec_from_weixin\\word2vec\\word2vec_wx'
    model = gensim.models.Word2Vec.load(fp)
    word_vec = model.wv
    # print(type(word_vec))
    # print(word_vec)
    dic = word_vec.vocab
    print(type(dic))
    dic_k = list(dic.keys())
    print(type(dic_k),len(dic_k))

    result = []
    for w in dic_k:
        print(w)
        v = word_vec[w].tolist()
        v = [str(item_v) for item_v in v]
        line = w + ' ' + ' '.join(v)
        line = line.strip()
        result.append(line)
    writeList2csv('./w2v.txt',result)
