#!/usr/bin python
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self,data=-1):
        self.data = data
        self.lc = None
        self.rc = None

class BST(object):
    def __init__(self):
        self.root = None# 初始化根节点为空

    def create_bst(self,datas):
        for data in datas:
            self.add_element(self.root,data)

    def add_element(self,root,data):
        cur = None# nxt为根节点，cur为nxt的父节点为空
        nxt = root# 注意出事两个变量的设置

        while nxt:# while作用找到带插入节点的父节点
            cur = nxt# 立即赋值
            if data<nxt.data:
                nxt = nxt.lc
            else:
                nxt = nxt.rc

        if cur==None:# 初始树为空时cur为空
            self.root = Node(data)
        else:
            if data<cur.data:# 上面只是找到待插入节点父节点，具体待插节点属于左、右子树还得判断
                cur.lc = Node(data)
            else:
                cur.rc = Node(data)

    def search_element(self,data):
        '''
            bst search
        '''
        if self.root==None:
            return None
        tar = self.root
        while tar:
            if data == tar.data:
                return tar.data
            elif data < tar.data:
                tar = tar.lc
            elif data > tar.data:
                tar = tar.rc
        return None
                
    def recursion_search_ele(self,root,data):
        if root==None:
            return None
        if root.data == data:
            return data
        elif data<root.data:
            return self.recursion_search_ele(root.lc,data)
        elif data>root.data:
            return self.recursion_search_ele(root.rc,data)

    def pre_recursion(self,root):
        rst = []
        if root==None:
            return None
        else:
            rst.append(root.data)
            if self.pre_recursion(root.lc):
                rst.extend(self.pre_recursion(root.lc))
            if self.pre_recursion(root.rc):
                rst.extend(self.pre_recursion(root.rc))
        return rst

    def middle_recursion(self,root):
        rst = []
        if root==None:
            return None
        else:
            if self.middle_recursion(root.lc):
                rst.extend(self.middle_recursion(root.lc))
            rst.append(root.data)
            if self.middle_recursion(root.rc):
                rst.extend(self.middle_recursion(root.rc))
        return rst

if __name__ == '__main__':
    t = [90,20,25,5,150]
    pre = [90,20,5,25,150]
    middle = [5,20,25,90,150]

    bst = BST()
    bst.create_bst(t)
    print('pre:',bst.pre_recursion(bst.root))
    print('middle:',bst.middle_recursion(bst.root))

    print(bst.search_element(25))
    print(bst.recursion_search_ele(bst.root,50))
















if __name__ == '__main__':
    pass









