#!/usr/bin python
# -*- coding:utf-8 -*-

"""
    priority queue + heap + heap order
"""
"""
    由于自身特点原因，完全二叉树的结构使用线性结构实现，python使用list
    堆的结构同完全二叉树，堆的实现也借助线性结构
    优先队列的实现依靠堆封装
"""

class Heap(object):
    def __init__(self,elems=None):
        self.elems = list(elems)

    def get_heap(self):
        return self.elems

    def init_heap(self):
        '''
           注意：初始化的时候从len(elems)//2的索引处开始，因为该索引向后的节点都认为已经是一个堆了
        '''
        elems = self.elems
        leng = len(elems)
        begin = leng//2
        for i in range(begin,-1,-1):    # 注意2：初始化的时候也要对根节点进行下沉操作
            e = elems[i]
            self.shiftdown(e,i,leng)

    def pop_top(self):
        elems = self.elems
        rst = elems[0]

        e = elems.pop()
        leng = len(elems)

        self.shiftdown(e,0,leng)
        return rst

    def shiftdown(self,e,father,end):
        elems,father,child = self.elems,father,(2*father)+1

        while child < end:
            if child +1 < end and elems[child] > elems[child+1]:    # 注意1：这里要判断child+1的范围
                child += 1
            if e < elems[child]:
                break
            elems[father] = elems[child]

            father,child = child,(2*child)+1
        elems[father] = e

    def add(self,e):
        elems = self.elems
        elems.append(e)

        leng = len(elems)
        self.shiftup(e,leng-1)

    def shiftup(self,e,end):
        elems,child,father = self.elems,end,(end-1)//2

        while child>0:
            if e < elems[father]:
                elems[child] = elems[father]

                child,father = father,(father-1)//2
        elems[child] = e

class PriorityQueue(object):
    def __init__(self,elems):
        self.heap = Heap(elems)

    def get_queue(self):
        self.heap.get_heap()

    def init_queue(self):
        self.heap.init_heap()

    def pop(self):
        self.heap.pop_top()


"""
    注意：
        1 需要明确，堆的功能就是确保每次弹出堆顶的元素是当前堆中权重的最值，对应小顶堆中，每次弹出的元素都是当前堆中的最小值
        2 弹出的元素需要存放，在不借助额外空间的情况下，将弹出的元素存放到线性结构对应尾部
        3 情况2的结果会造成线性结构从左至右是降序的，在这种情况下需要以O(n)再遍历一遍线性结构
"""
def heap_order(nums):
    # 初始化堆
    pass
    # order





if __name__ == '__main__':
    nums = [4, 2, 6, 3, 2, 1]
    ## 堆排序
    heap_order(nums)
    exit(0)
    ## 堆的测试
    heap = Heap(nums)
    heap.init_heap()
    print(heap.get_heap())  #[1, 2, 4, 3, 2, 6]

    top_num = heap.pop_top()
    print(top_num)  # 1
    print(heap.get_heap()) # [2, 2, 4, 3, 6]







