#!/usr/bin python
# -*- coding:utf-8 -*-

import pandas as pd
import os

if __name__ == '__main__':
    pd.set_option('display.width', 5000)
    pd.set_option('display.max_columns', None)

    outDir = '/opt/workspace/antcolony_update/datasets/sessions'

    # fnameList = ['2017-05.csv','2017-04.csv','2017-03.csv','2017-01.csv']
    fnameList = os.listdir(outDir)

    resultList = []
    for fname in fnameList:
        fpath = os.path.join(outDir,fname)

        df = pd.read_csv(fpath)
        series = df['1_date'].groupby(df['0_label']).count()

        resultList.append([series[0],series[1]])

    column = ['no','yes']
    df_stat = pd.DataFrame(resultList,columns=column)
    print(df_stat)

    no_sum = df_stat['no'].sum()
    yes_sum = df_stat['yes'].sum()
    print('no_sum:',no_sum)
    print('yes_sum:',yes_sum)