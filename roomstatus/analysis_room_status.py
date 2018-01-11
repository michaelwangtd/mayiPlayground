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

df = pd.read_csv('./2017-05.csv')
# print(df)
# re = df.groupby('0_label').count()
re = df['1_date'].groupby(df['0_label']).count()
print(re)