#!/usr/bin python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

if __name__ == '__main__':
    pd.set_option('display.width',5000)

    df = pd.DataFrame({'key1':['a','a','b','b','a'],\
                  'key2':['one','two','one','two','one'],\
                  'd1':np.random.randn(5),\
                  'd2':np.random.randn(5)
                  })
    print(df)
    gdk1 = df['d1'].groupby(df['key1'])
    # print(type(gdk1))
    # print(gdk1)
    print(gdk1.mean())
    """
    key1
    a   -0.466118
    b    1.637663
    Name: d1, dtype: float64
    """
    print(gdk1.sum())

    gdk2 = df['d2'].groupby([df['key1'],df['key2']])
    # print(gdk2.mean())
    # print(gdk2.mean().unstack())
    """
    key2       one       two
    key1                    
    a    -0.031110 -1.248988
    b    -0.060531 -0.932921
    """