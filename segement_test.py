#!/usr/bin python
# -*- coding:utf-8 -*-

import jieba

jieba.load_userdict('./dic/userdic.txt')

tStr = '过来求医，想要预订10月09日-10月19日的房，共10天，请问这个时间方便接待吗'
tStr = '做饭可以的，但是没有调味品和食材'
tStr = '我这只有1.8*2   1.2*2和一个单人沙发床，能住下吗？麻将目前没有'
tStr = '急急急2017-11-01我来入住'
print(list(jieba.cut(tStr)))
