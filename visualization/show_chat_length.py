#!/usr/bin python
# -*- coding:utf-8 -*-

from matplotlib import pyplot as plt
from utils import fileops
import pandas as pd
import matplotlib as mpl

if __name__ == '__main__':
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    chatLenList = fileops.loadPickle('../pickle/chatLen.pkl')

    df = pd.DataFrame(chatLenList)
    X = df[0]
    Y = df[1]
    print(df[[0,1]])
    # print(X)
    # print(Y)

    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(X,Y,'r.')
    plt.title('折线图')
    plt.xlabel('聊天长度')
    plt.ylabel('文件个数')
    plt.subplot(2, 1, 2)
    plt.plot(X, Y, 'g-')
    plt.title('折线图')
    plt.xlabel('聊天长度')
    plt.ylabel('文件个数')
    plt.show()