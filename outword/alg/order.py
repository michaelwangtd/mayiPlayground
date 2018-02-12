#!/usr/bin python
# -*- coding:utf-8 -*-

import os
"""
    使用python实现一遍排序算法，再次复习时间、空间复杂度
"""

"""
    1 归并排序的最好、最坏和平均时间复杂度都是O(nlogn)，而空间复杂度是O(n)
    2 归并排序算法比较占用内存，但却是效率高且稳定的排序算法
"""

# merge order
def merge_order(nums,low,high):
    if low < high:
        # mid = (low+high)//2
        mid = (low+high)>>1 # 注意：这里移位的次数
        merge_order(nums,low,mid)
        merge_order(nums,mid+1,high)
        merge(nums,low,mid,high)

def merge(nums,low,mid,high):
    i,j,k = low,mid+1,0
    m,n = mid,high
    temp = []
    while i<=m and j<=n:
        if nums[i]<nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i<=m:
        temp.append(nums[i])
        i += 1
    while j<=n:
        temp.append(nums[j])
        j += 1
    nums[low:high+1] = temp



if __name__ == '__main__':
    nums = [3,5,2,1,7,4]
    # nums = [3,5,2]

    merge_order(nums,0,len(nums)-1)
    print(nums)
