#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops

if __name__ == '__main__':
    datas = fileops.readListFromTxt('./data/q.txt')
    print(len(datas))
    for word in datas:
        if '几' in word:
            print(word)