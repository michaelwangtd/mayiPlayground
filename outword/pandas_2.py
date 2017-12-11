#!/usr/bin python
# -*- coding:utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

if __name__ == '__main__':
    pd.set_option('display.max_columns',None)#全部展示数据

    ## create2csv
    data = {
        'date':pd.date_range('20171101',periods=10),
        'gender':np.random.randint(0,2,size=10),
        'height':np.random.randint(40,50,size=10),
        'weight':np.random.randint(150,180,size=10)
    }
    df = DataFrame(data)
    # df.to_csv('./data.csv')
    ## readfromcsv
    df = pd.read_csv('./data.csv')
    # print(df)
    """
    Unnamed: 0        date  gender  height  weight
    0           0  2017-11-01       0      47     154
    1           1  2017-11-02       1      46     162
    2           2  2017-11-03       0      43     168
    3           3  2017-11-04       1      47     158
    4           4  2017-11-05       1      41     152
    5           5  2017-11-06       0      44     156
    6           6  2017-11-07       1      45     175
    7           7  2017-11-08       0      48     171
    8           8  2017-11-09       1      43     179
    9           9  2017-11-10       0      48     166
    """
    # print(type(df.values))
    # print(df.values)
    """<class 'numpy.ndarray'>
[[0 '2017-11-01' 1 46 160]
 [1 '2017-11-02' 1 45 158]
 [2 '2017-11-03' 0 40 179]
 [3 '2017-11-04' 1 41 151]
 [4 '2017-11-05' 1 44 162]
 [5 '2017-11-06' 0 45 150]
 [6 '2017-11-07' 0 49 172]
 [7 '2017-11-08' 1 48 153]
 [8 '2017-11-09' 1 41 165]
 [9 '2017-11-10' 0 49 178]]"""
    # print(df.index)#RangeIndex(start=0, stop=10, step=1)
    # print(df.index.name)#None

    # print(df.columns)#Index(['Unnamed: 0', 'date', 'gender', 'height', 'weight'], dtype='object')
    # print(df.columns.name)#None

    # print(df.head(2))
    # print(df.tail(2))
    """   Unnamed: 0        date  gender  height  weight
       0           0  2017-11-01       0      49     158
       1           1  2017-11-02       1      40     164
   Unnamed: 0        date  gender  height  weight
       8           8  2017-11-09       0      41     175
       9           9  2017-11-10       0      46     159"""

    # print(df.describe())
    """
           Unnamed: 0     gender     height      weight
    count    10.00000  10.000000  10.000000   10.000000
    mean      4.50000   0.600000  44.200000  159.400000
    std       3.02765   0.516398   3.794733   10.079683
    min       0.00000   0.000000  40.000000  150.000000
    25%       2.25000   0.000000  41.000000  152.500000
    50%       4.50000   1.000000  43.500000  156.500000
    75%       6.75000   1.000000  47.750000  161.750000
    max       9.00000   1.000000  49.000000  178.000000
    """

    # print(df[0:4])
    """
       Unnamed: 0        date  gender  height  weight
    0           0  2017-11-01       0      40     169
    1           1  2017-11-02       0      41     161
    2           2  2017-11-03       0      44     171
    3           3  2017-11-04       0      44     157
    """

    # 按照索引选择数据
    # print(df.loc[:,['gender','height']])
    """
       gender  height
    0       0      47
    1       0      48
    2       1      41
    3       1      43
    4       1      43
    5       0      46
    6       1      43
    7       0      45
    8       1      42
    9       0      49
    """
    # 按照行、列选择数据
    # print(df.iloc[0:4,2:4])
    """
       gender  height
    0       1      44
    1       0      42
    2       0      43
    3       1      44
    """

    # print(df['gender'].value_counts())
    # print(df['height'].median())
    # print(df.mean())
    """
    Unnamed: 0      4.5
    gender          0.5
    height         44.1
    weight        169.6
    dtype: float64
    """
    # print(df['weight'].std())

    # 统计非NA值的个数
    # print(df.count())
    """
    Unnamed: 0    10
    date          10
    gender        8
    height        9
    weight        8
    dtype: int64
    """

    # print(df['gender'])
    """
    0    0.0
    1    1.0
    2    NaN
    3    1.0
    4    NaN
    5    0.0
    6    NaN
    7    NaN
    8    0.0
    9    NaN
    Name: gender, dtype: float64
    """
    # print(df['gender'].dropna())
    """
    0    0.0
    1    1.0
    3    1.0
    5    0.0
    8    0.0
    Name: gender, dtype: float64
    """
    # print(df['gender'].fillna(value=0))
    """
    0    0.0
    1    1.0
    2    0.0
    3    1.0
    4    0.0
    5    0.0
    6    0.0
    7    0.0
    8    0.0
    9    0.0
    Name: gender, dtype: float64
    """

    # 基于行、列频数的统计
    # print(pd.crosstab(df['weight'],df['gender']))
    """
    gender  0.0  1.0
    weight          
    152.0     1    0
    165.0     0    1
    167.0     0    1
    168.0     2    0
    """

    # print(df.drop([0,2,4,6,8], axis=0))  # 删除行，注意原数据不变，返回一个新数据
    """
       Unnamed: 0        date  gender  height  weight
    1           1   2017/11/2     1.0    48.0   165.0
    3           3   2017/11/4     1.0     NaN   167.0
    5           5   2017/11/6     0.0    46.0   168.0
    7           7   2017/11/8     NaN    49.0   164.0
    9           9  2017/11/10     NaN    40.0   162.0
    """

    # print(df.drop(['gender','height','weight'], axis=1))  # 删除列，inplace=True表示直接在原数据修改而不新建对象
    """
       Unnamed: 0        date
    0           0   2017/11/1
    1           1   2017/11/2
    2           2   2017/11/3
    3           3   2017/11/4
    4           4   2017/11/5
    5           5   2017/11/6
    6           6   2017/11/7
    7           7   2017/11/8
    8           8   2017/11/9
    9           9  2017/11/10
    """

    # concat
    """
    相同字段的表首尾相接
    result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z']) //keys给合并的表来源加一个辨识号
    注意多张表concat后可能会出现index重复情况，这是最好使用reset_index重新组织下index。
    result.reset_index(drop=True)
    """

    # 数据数值化 map()
    d = Series(['a','a','b','a','b'])
    # print(d)
    map_dic = {'a':1,'b':0}
    # print(d.map(map_dic))
    """
    0    a
    1    a
    2    b
    3    a
    4    b
    dtype: object
    0    1
    1    1
    2    0
    3    1
    4    0
    dtype: int64
    """






