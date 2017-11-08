#!/usr/bin python
# -*- coding:utf-8 -*-

import jieba
from utils import fileops
import index


if __name__ == '__main__':
    jieba.load_u

    answerWL = fileops.readListFromTxt(index.rootdir+'/dic/answer_feature_word.txt')
