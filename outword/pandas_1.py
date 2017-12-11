#!/usr/bin python
# -*- coding:utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame

if __name__ == '__main__':

    ## Series
    """具有数组、字典功能"""
    # 1
    t1 = ['a','b','c','d']
    d1 = Series(t1)
    # print(type(d1))#<class 'pandas.core.series.Series'>
    # print(d1.index)#RangeIndex(start=0, stop=4, step=1)
    # print(d1.values)#['a' 'b' 'c' 'd']
    # print(d1)
    """
    0    a
    1    b
    2    c
    3    d
    dtype: object
    """
    # print(d1.isnull)
    t2 = [1,2,3,4]
    d2 = Series(t2,index=t1)
    # print(d2)
    """
    a    1
    b    2
    c    3
    d    4
    dtype: int64
    """
    # 2 使用append连接其他Series
    d3 = Series(t2)
    # print(d3)
    """
    0    1
    1    2
    2    3
    3    4
    dtype: int64
    """
    dt = Series([5,6])
    d4 = d3.append(dt,ignore_index=True)
    # print(d4)
    """
    0    1
    1    2
    2    3
    3    4
    0    5
    1    6
    dtype: int64
    """
    d5 = d4.drop(0)#按照索引index删除
    # print(d5)
    """
    1    2
    2    3
    3    4
    4    5
    5    6
    dtype: int64
    """
