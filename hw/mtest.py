#!/usr/bin python
# -*- coding:utf-8 -*-

import numpy as np

t1 = np.array([1,2,3])
t2 = np.array([1,2,3])
re = t1*t2
re2 = np.multiply(t1,t2)
print(re)
print(re2)


# re = np.random.randn(4,3)
# print(re.shape)
# print(re)
# re2 = np.zeros((4,3))
# print(re2.shape)
# print(re2)