#!/usr/bin python
# -*- coding:utf-8 -*-

import sklearn
import re
from queue import Queue
import time
from datetime import datetime
from pandas import Series,DataFrame
import pandas as pd
import numpy as np







# t = 'abcd'
# for i,v in enumerate(t):
#     print(i,v)




#1244
# print(1243-755)
# print(1785-1243)
# print(7063-542)
# print(6521-488)
# print(1243-488)
# print(1-(755/6033))



# print(1776-1287)
# print(7042-489)
# print(1287-791)
#
# print(6553-496)
# print(1287-496)

# print(1-(791/6057))



# print(1-(1731/6962))
# print(1-(758/6962))
# # print(6962-494)
# print(1-(1237/6468))
# print(1-(758/6468))


# print(1691-478)
# print(1-(1213/6468))



# print(6468-479)
#
# print(1-(1237/6468))
#
# print(1-(758/5989))


# print(1237-758)


# t1 = '888A999A123'
# t2 = '888A999A213'
# if t1>t2:
#     print(t1)
# elif t1<t2:
#     print(t2)

# print(1700/4)
# print(425/60)



# t = 'sjdskjf'
# print(t[:2])


# np.random.rand()
# np.random.randn()


# if __name__ == '__main__':
#     pd.set_option('display.width',5000)
#
#     df = pd.DataFrame({'key1':['a','a','b','b','a'],\
#                   'key2':['one','two','one','two','one'],\
#                   'd1':np.random.randn(5),\
#                   'd2':np.random.randn(5)
#                   })
#     # print(df)
#
#     re = df['d1'].groupby(df['key1']).sum()
#     # print(re)
#
#     for idx in df.index:
#         print('--------------------')
#         print(type(df.loc[idx]),df.loc[idx])
#         print(type(df.loc[idx].values),df.loc[idx].values)
#         break



# df = pd.read_csv('./noroom_deleted_fw.txt',header=None)
# df = df[0].values[:]
# print(type(df))
# print(df)
# if '顶完' in df:
#     print('true')



# ds2 = [[1,2],[3,4],[5,6]]
# ds2 = np.asarray(ds2)
# print(type(ds2))
# df2 = pd.DataFrame(ds2,columns=['a','b'])
# print(type(df2))
# print(df2)
# df2.to_csv('./df2_test.csv')




# t = [[1,2],[2,3],[3,4],[4,5]]
# print(type(t))
# t = pd.DataFrame(t)
# print(type(t))
# print(t)



# print(8/5*100)
# print(160/60)


# print(15/100)


# t = ['a','b','c']
#
# print(t[0])
# print(''.join(t[1:]))





# t = Series([1,2,3,4])
# for v in t:
#     print(type(v),v)



# print(517-141+63)



# print(517*20)


# def getOrderedSeries(inSeries):
#     resultList = []
#     for item in inSeries:
#         if isinstance(item,float):
#             resultList.append(item)
#         elif isinstance(item,str):
#             cakeList = item.strip().split('\n')
#             cakeList = [cake.split(':') for cake in cakeList]
#             cakeList = sorted(cakeList,key=lambda item: item[-2])
#             cakeList = [':'.join(cake) for cake in cakeList]
#             cakestr = '\n'.join(cakeList)
#             resultList.append(cakestr)
#     return Series(resultList)






# t1 = [1,2,3,4,5,6]
# t2 = [2,3,4]
# re = set(t1).difference(set(t2))
# print(re)
# print(type(re))



# date = datetime.now().strftime('%Y-%m-%d')
# print(date)


# tStr = '12'
# # print(len(tStr))
# print(tStr[:2])



# # str = 'landlord:20-22可以'
# str = 'landlord: 23.24号没有房间了你看的这间已经被预定了的'
#
# # rex = '\d+[到至-\～\~]d+'
# # rex = '\d+[\-\~\～到至]\d+'
# # rex = '\d+'
# rex = '\d+[\.\,\，\,\、]\d+[号日]'
# reResult = re.findall(rex,str,re.S)
# print(reResult)


# tStr = '没有 2017'
# rightSent = tStr.replace(' ','')
# rightSent = re.sub('\d*','',rightSent)
# rightSent.replace('！','').replace('，','').replace(',','').replace('。','') \
#     .replace('？', '').replace('?','').replace('、','').replace('[','')


# date = '2016-11-16'
# re = time.mktime(time.strptime(date,'%Y-%m-%d'))
# print(re)
# retime = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(date,'%Y-%m-%d'))
# print(retime)




# que = Queue()
# testList = ['1','2','3','4','1','2','3']
# for item in testList:
#     if not item in que:
#         que.put(item)
# while not que.empty():
#     print(que.get())




# session = 'sfds 环境开会系统检测到您在对话中提到“没有房”，已自动帮您把10月1日的房态置为无房。'
# if re.search('系统检测到您在对话中.*',session,re.S):
#     print('ok')



# line = '7月30日、31日'
# line = '7月30日、31日、32日'
# re31 = '\d+月(\d+[号日號][\、]){1,}'
# if re.findall(re31,line,re.S):
#     print(re.findall(re31,line,re.S))


# line = '您好，我们一行，过来旅游，想要预定12月31日-01月01日的房，共，请问这个时间方便接待吗?'
#
# re1 = '\d+个人|\d+分钟|\d+元|\d+个半|\d*点|价格是\d+|\d+层|一宿\d+|\d+m|\d+米\d+|\d+站|\d+楼|'
# re2 = '^您好，我们一行.*'
#
# line = re.search(re2,line,re.S)
# print(line)


# tStr = '877898'
# if re.search('^\d+$',tStr,re.S):
#     print(tStr)


# tStr = '26.27.28三天'
#
# re1 = '\d+\.\d+\.\d+三.'
# re2 = '\d+\.\d+\.\d+[(三天)|(号)]|\d{3,6}号'
#
# if re.findall(re2, tStr, re.S):
#     reMatchList = re.findall(re2, tStr, re.S)
#     print(reMatchList)



    # tstr = '我是按照你10.16到11，14号退算的价格'
# tstr = '过来旅游，想要预订4号到6号的房，共2天，请问这个时间方便接待吗?'
# q = '|\d*[.|,|，]\d*[-|到|～]\d*[.|,|，]\d*'
# res = re.findall('(\d+月\d+日-\d+月\d+日|\d+号到\d+号|\d+，\d+号|\d+～\d+号|\d+、\d+号|\d+,\d+号|\d{3,6}号|\d+.\d+.\d+号|\d+[.|,|，]\d+[-|到|～]\d+[.|,|，]\d+)', tstr, re.S)
# print(res)


# tstr = '打算是从23-28日'
# res = re.findall('((\d+月\d+日\-\d+月\d+日)|(\d+号到\d+号)|(\d+，\d+号)|(\d+\～\d+号)|(\d+\、\d+号)|(\d+\,\d+号)|'
#                   '(\d{3,6}号)|(\d+\.\d+\.\d+号)|(\d+[\.|\,|\，]\d+[\-|到|\～]\d+[\.|\,|\，]\d+[|号])|'
#                   '(\d+\.\d+)|(\d+[到|\-|\～]\d+[日|号])|(\d+月\d+[日|号][\-|至|到|\～]\d+[日|号]))', tStr, re.S)
# print(res)
#
#
#
# re.findall('(\d+月\d+日\-\d+月\d+日|\d+号到\d+号|\d+，\d+号|\d+\～\d+号|\d+\、\d+号|\d+\,\d+号|'
#                   '\d{3,6}号|\d+\.\d+\.\d+号|\d+[\.|\,|\，]\d+[\-|到|\～]\d+[\.|\,|\，]\d+[|号]|'
#                   '\d+\.\d+|\d+[到|\-|\～]\d+[日|号]|\d+月\d+[日|号][\-|至|到|\～]\d+[日|号])', tStr, re.S)




# re.findall('(\d*月\d*日-\d*月\d*日|\d*号到\d*号|\d*，\d*号|\d*～\d*号|\d*、\d*号|\d*,\d*号|\d{3,6}号|\d*.\d*.\d*号|\d*[.|,|，]\d*[-|到|～]\d*[.|,|，]\d*)', tStr, re.S):



# print(len('1234'))
# tstr = '1234'
# print(tstr[2:4])


# for i in range(4,7):
#     print(i)



# test = '4、5号有人'
#
# if re.findall('(\d.*?)',test,re.S):
#     reList = re.findall('(\d.*?)',test,re.S)
#     print(reList)




# print(170+194)


# tStr = '这套1号被订，正好空2，3号两天，4～7号被订了'
# result = re.findall('(号.*号)',tStr,re.S)
# print(type(result),len(result))
# print(result)

# print(64393/83762)

# print(184+326-77)

# print(508-465)

# print(254+149)

# testList = [['tenant', 'TAT'], [':', 'O'], ['你好', 'O'], ['，', 'O'], ['可以', 'O'], ['把', 'O'], ['门锁', 'O'], ['的', 'O'], ['密码', 'O'], ['给', 'O'], ['我', 'O'], ['吗', 'O']]
# l1,l2 = list(zip(*testList))
# print(l1,type(l1))
# print(l2)





# t1 = [['tenant', 'TAT'], [':', 'A'], ['你好', 'O'], ['，', 'O']]
#
# t2 = [['tenant', 'TAT'], [':', 'O'], ['你好', 'O'], ['，', 'O']]
#
# for i in range(len(t1)):
#     if not t1[i]==t2[i]:
#         print(t1[i],t2[i])



# print(326+186)




# words = [['a','b','c'],['d','e'],['f','g','h'],['i']]
# tags = [[1,2,3],[1,2],[1,2,3],[1]]
#
# re = list(zip(words,tags))
# print(re)




# def isQuestion(wordList):
#     questionList = ['吗','是不是','呢','？','?','几','为啥','在么','怎么','什么']
#     # whiteList = ['没什么']
#
#     intersection = list(set(wordList).intersection(set(questionList)))
#     # print(intersection)
#     if intersection:
#         return True
#     else:
#         return False
#
# wordList = ['在','哪里','呀','吗','为啥']
# print(isQuestion(wordList))



# print(212+93)