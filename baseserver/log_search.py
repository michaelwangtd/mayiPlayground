#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops
import re

if __name__ == '__main__':
    fw = open('../data/traceinit_analysis.log','w',encoding='utf-8')
    fr = open('../data/traceinit.log','r',encoding='utf-8')
    i = 1
    while True:
        line = fr.readline()
        if line:
            line = line.strip()
            re1 = '\d+\-\d+\-\d+\s*\d+\:\d+\:\d+\s*\-\s*DEBUG\s*\-\s*houseinventory.py\[line\:\d+\]\s*\-\s*'
            if re.search(re1,line,re.S):
                line = re.sub(re1,'',line)
                if line[0] != '[' and line[1] != ']':
                    if 'tenant' in line or 'landlord' in line:
                        if re.search('(\d+)',line,re.S):
                            print(i,line)
                            fw.write(line + '\n')
                            i += 1
    fr.close()
    fw.close()