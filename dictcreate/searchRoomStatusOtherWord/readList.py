#!/usr/bin python
# -*- coding:utf-8 -*-

import json
from utils import fileops
import jieba
import re
import pandas as pd

dataPath = 'D:\workstation\\repositories\mayiPlayground\dictcreate\searchRoomStatusOtherWord\\'
wordList = fileops.readListFromTxt(dataPath+'meiyou.txt')
# print(len(wordList))
print(str(wordList))