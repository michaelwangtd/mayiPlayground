#!/usr/bin python
# -*- coding:utf-8 -*-

import os
"""
    使用python实现一遍排序算法，再次复习时间、空间复杂度
"""

def merge_order(nums,start,end):
    if start<end:
        mid = (start+end)>>2
        merge_order(nums,start,mid)
        merge_order(nums,mid,end)
        merge(larr,rarr)

def merge(larr,rarr):
    pass




if __name__ == '__main__':
    nums = [3,5,2,1,7,4]
