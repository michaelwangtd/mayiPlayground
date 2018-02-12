#!/usr/bin python
# -*- coding:utf-8 -*-

from collections import deque
from collections import Counter
import numpy as np
import random
import math

class ListNode(object):
    def __init__(self,n=None):
        self.val = n
        self.next = None

class TreeNode(object):
    def __init__(self,n=None):
        self.val = n
        self.left = None
        self.right = None








t = [1,2,3]
def permute(nums):













# class Solution(object):
#     def sortList(self, head):
#         if head == None or head.next == None:
#             return head
#         mid = self.get_middle_node(head)
#         nxt = mid.next
#         mid.next = None
#         return self.merge_list(self.sortList(head),self.sortList(nxt))
#
#     def merge_list(self,ha,hb):
#         dummy = cur = ListNode(-1)
#         while ha and hb:
#             if ha.val<hb.val:
#                 cur.next = ha
#                 ha = ha.next
#             else:
#                 cur.next = hb
#                 hb = hb.next
#             cur = cur.next
#         cur.next = ha if ha else hb
#         head = dummy.next
#         dummy.next = None
#         return head
#
#     def get_middle_node(self,head):
#         slow = fast = head
#         while fast.next != None and fast.next.next != None:
#             fast = fast.next.next
#             slow = slow.next
#         return slow

# t = [1,2,3,4,5]



# def inorderTraverse(root):
#     stack = []
#     rst = []
#     while root or stack:
#         while root:
#             stack.append(root)
#             root = root.left
#         node = stack.pop()
#         rst.append(node.val)
#         root = node.right
#     return rst

# def inorderRecursion(root):
#     if root != None:
#         inorderRecursion(root.left)
#         print(root)
#         inorderRecursion(root.right)


# t1 = ListNode(1)
# t2 = ListNode(2)
# t3 = ListNode(3)
# t4 = ListNode(4)
# t5 = ListNode(5)
# t1.next = t2
# t2.next = t3
# t3.next = t4
# t4.next = t5
# head = t1


# print((0+2)>>2)
# print((0+2)//2)

# print(4>>1>>1)
# print(2>>1)


# class Ball(object):
#     def __init__(self,nums,snum):
#         self.nums = nums
#         self.snum = snum
#         print(self.nums)
#         print(self.snum)
#     def print_nums(self):
#         print(self.nums)
#         print(self.snum)
#     def del_item(self):
#         temp = self.nums
#         temp.append('end')
#         temp.pop(0)
#
#         t2 = self.snum
#         t2 = 'end'
# '''
# ['begin', 1, 2]
# begin
# [1, 2, 'end']
# begin
# '''
# ball = Ball(['begin',1,2],'begin')
# ball.del_item()
# ball.print_nums()

# def groupAnagrams(strs):
#     """
#     :type strs: List[str]
#     :rtype: List[List[str]]
#     """
#     dic = {}
#     if strs:
#         for itm in strs:
#             bit = [0]*26
#             word = list(itm)
#             for w in word:
#                 idx = ord(w)-ord('a')
#                 bit[idx] += 1
#             bit = str(bit)
#             if bit not in dic:
#                 dic[bit] = []
#             dic[bit].append(''.join(word))
#     rst = []
#     if dic:
#         for k, v in dic.items():
#             if v:
#                 rst.append(v)
#     return rst
# # strs = ["eat","tea","tan","ate","nat","bat"]
#
# strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
# print(groupAnagrams(strs))



# tc < n^2
# sc = 1
# t = [1,1]
# t = [1,2,3,4,5,1]
# t = [1,2,1,1,5,1]


# t = [1,2,3,4,5]

# print(5/2)
# t = [1,2,5,5,3,5]
# def findDuplicate(nums):
#     low,high = 1,len(nums)-1
#     while low < high:
#         mid = (low+high)>>1
#         count = 0
#         for itm in nums:
#             if itm <= mid:
#                 count += 1
#         if count > mid:
#             high = mid
#         else:
#             low = mid + 1
#     return low


# def findDuplicate(nums):
#     if len(nums) == 0:
#         return 0
#     low = 1
#     high = len(nums)
#     while low < high:
#         mid = low + int((high-low)>>1)
#         count = 0
#         for x in nums:
#             if x <= mid:
#                 count = count + 1
#         if count > mid:
#             high = mid
#         else:
#             low = mid+1
#     return low
# print(findDuplicate(t))

# print((4+5)>>1)





# t = [1,2,3,4,5]
# def oddevenlist(head):
#     odd = ListNode(0)
#     even = ListNode(0)
#     odd_cur,even_cur = odd,even
#     cur = head
#     i = 1
#     while cur:
#         nxt = cur.next
#         if i%2==0:
#             even_cur.next = cur
#             even_cur = even_cur.next
#         else:
#             odd_cur.next = cur
#             odd_cur = odd_cur.next
#         cur.next = None
#         cur = nxt
#         i += 1
#     odd_cur.next = even.next
#     head = odd.next
#     odd.next = None
#     return head
#
# oddevenlist(head)



# t = [1,2,3,4,5]
# def ini(t):
#     root = TreeNode(t.pop(0))
#     queue = [root]
#     while t:
#         node = queue.pop(0)
#         if node.left==None and t:
#             queue.append(TreeNode(t.pop(0)))
#         if node.right==None and t:
#             queue.append(TreeNode(t.pop(0)))
#     return root
# root = ini(t)
# print(root.val)


# t = [5, 4, 3, 2, 1]
# v = [1,2,3,4,5]
# # d = zip(t,v)
# # print(d)
#
# r = [0]*len(v)
# print(r)

# for i in range(len(t),0,-1):
#     print(i)

# t = [1,2,3,4,5]
# rst = [1,3,5,2,4]
# def oddeven_list(head):
#     odd = even = ListNode(0)
#     odd_cur,even_cur = odd,even
#     cur = head
#     i = 1
#     while cur:
#         if i%2==0:
#             even_cur.next = cur
#             even_cur = even_cur.next
#         else:
#             odd_cur.next = cur
#             odd_cur = odd_cur.next
#         cur = cur.next
#         i += 1
#     odd_cur.next = even.next
#     even.next = None
#
# n = 5+1
# t = [1,2,3,4,1,5]
# # t = [1,2,1,1,5,3]
#
# def find_duplicate_one(t):
#     pass




# t = [5, 4, 3, 2, 1]
# t = [1,2,3,4,5]
# t = [5,1,5,5,2,5,4]
# def have_increase_tripe(nums):
#     count = 0
#     for i in range(len(nums)-1):
#         if nums[i]<nums[i+1]:
#             count += 1
#         else:
#             count = 0
#         if count==2:
#             return True
#     return False


# def _level_traverse(root):
#     queue = []
#     queue.append(root)
#     rst = []
#     while queue:
#         node = queue.pop(0)
#         rst.append(node.val)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

# def level_traverse(root):
#     if root==None:
#         return None
#     queue = [root]
#     rst = []
#     while queue:
#         rst.append([nd.val for nd in queue])
#         temp = []
#         while queue:
#             node = queue.pop(0)
#             if node.left:
#                 temp.append(node.left)
#             if node.right:
#                 temp.append(node.right)
#         queue = temp
#     return rst



# t = [1,2,3,4,5]
#
# def shuffle(l):
#     leng = len(l)
#     for i in range(leng):
#         j = i
#         while i == j:
#             j = math.floor(random.random()*leng)
#         l[i],l[j] = l[j],l[i]
#     return l
# print(shuffle(t))


# i = 0
# n = 2
# while i<5:
#     rst = random.random()
#     print(rst)
#     print(rst*(n))
#     print(math.floor(rst*(n)))
#     i += 1

# rd = random.random()*(n+1)
# print(rd)
# rd = math.floor(rd)
# print(rd)


# t1 = ListNode(1)
# t2 = ListNode(2)
# t3 = ListNode(3)
# t4 = ListNode(2)
# t5 = ListNode(1)
# t1.next = t2
# t2.next = t3
# t3.next = t4
# t4.next = t5
# head = t1

# t = [1,2,3,2,1]
# t = [1,1]
# t = [1]

# def detect_node(head):
#     fast = slow = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow
# def get_reversed_end_part_head(middle):
#     pre = None
#     cur = middle
#     while cur:
#         nxt = cur.next
#         cur.next = pre
#         pre = cur
#         cur = nxt
#     return pre
# def is_palindrome_linkedlist(head):
#     middle = detect_node(head)
#     if middle is head:
#         return True
#     end_head = get_reversed_end_part_head(middle)
#     while head is not middle:
#         if head.val != end_head.val:
#             return False
#         head = head.next
#         end_head = end_head.next
#     return True


# t = [1,2,3,4]
# s = [24,12,8,6]

# s = 'jaksjf'
# s = list(s)
# t = '*'*5
# print(t)
# print(len(t))
# s[1:2]='*'*2
# print(s)


# tt = [1,2,3,4]
# 1,2 3,4
# 1,2 3 4,5

# d = {'1':'2','2':'3'}
# print(d.get('3'))

# def over(nums):
#     if not nums:
#         return None
#     i,j = 0,len(nums)-1
#     while i<=j:
#         temp = nums[j]
#         nums[j] = nums[i]
#         nums[i] = temp
#         i += 1
#         j -= 1
#     return nums

# t = 6754
# b_t = bin(t)
# print(typeb_t)

# t1 = [2,3]
# t2 = [1,1,4]

# t1 = [1,1,2,3,4]
# t2 = [5]
#
# t1.remove(1)

# def merge(nums1, m, nums2, n):
#     if (not nums1 and nums2) or (m==0 and n>0):
#         while nums1:
#             nums1.pop()
#         nums1.extend(nums2)
#     if m>0 and n>0:
#         print('------------')
#         i = j = 0
#         while j<n:
#             if nums2[j]<=nums1[i]:
#                 nums1.insert(i,nums2[j])
#                 i += 1
#             else:
#                 while i<len(nums1) and nums1[i]<nums2[j]:
#                     i += 1
#                 nums1.insert(i,nums2[j])
#             j += 1
#
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# merge(nums1, m, nums2, n)
# print(nums1)


# def rotate(nums, k):
#     if len(nums)>1 or k>0:
#         nums = over(nums)
#         nums[:k] = over(nums[:k])
#         nums[k:] = over(nums[k:])
#
# t = [1,2]
# k = 0



# def mergeList(l1,l2):
#     if not l1 or not l2:
#         return l1 or l2
#     #
#     dummy = cur = ListNode(-1)
#     while l1 and l2:
#         if l1.val<l2.val:
#             cur.next = l1
#             cur = cur.next
#             l1 = l1.next
#         else:
#             cur.next = l2
#             cur = cur.next
#             l2 = l2.next
#     cur.next = l1 or l2
#     head = dummy.next
#     dummy.next = None
#     return head


# nums = [1,1,2]
# leng = len(nums)

# t = ['1',
# '11',
# '21',
# '1211',
# '111221']

# def trailingZeroes(n):
#     r = 0
#     while n > 0:
#         n /= 5
#         print(n)
#         r += n
#     return r
# print(trailingZeroes(5))

#
# print(7/5)

# t1 = '12u jd'
# for t in t1:
#     print(t.isdigit())
#     print(t.isalpha())
#     print(t.isspace())
#     print('---------')
# exit(0)

# t = 'adsfasf'
# print(type(t))
# print(type(list(t)))

# t = ''
# if t:
#     print('you')
# exit(0)
# t = 'jsfs'
# print(list(t))

# n = 3
# print(3*2*1)
# def factorial_recursion(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*factorial_recursion(n-1)
# rst = factorial_recursion(3)
#
#
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     rst = 1
#     for i in range(2,n+1):
#         rst *= i
#     return rst
# rst = factorial(3)
# print(rst)
#
#
#
#
# def factorial_ending(n):
#     if n == 0 or n == 1:
#         num = 1
#     else:
#         num = 1
#         for i in range(2,n+1):
#             num *= i
#
#     count = 0
#     num = list(str(num))
#     while num:
#         end = num.pop()
#         if end != '0':
#             break
#         count += 1
#     return count
# print(factorial_ending(4))



# s1 = '房子面积多大 厨卫都是独立的吧 要能自己做饭 ,我们有两种户型 一种是电磁炉的，您这个价格可以'
# s2 = '小床多小 路程一样吗 '
# s3 = 'abcdedcba'
# s4 = 'A man, a plan, a canal: Panama'
# s5 = 453000
# l1 = '房子'
# l2 = '有'
# rel = s2.strip().split(' ')
# print(rel)
# s = s4
# s = '.'
# def hw(s):
#     s = list(s.strip())
#     if not s or len(s)==1:
#         return True
#     i,j = 0,len(s)-1
#     while i<=j:
#         while i<len(s) and not s[i].isalpha():
#             i += 1
#         while j>0 and not s[j].isalpha():
#             j -= 1
#         if i>j:
#             return False
#         s[i],s[j] = s[i].lower(),s[j].lower()
#         if s[i]!=s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
# print(hw(s))



# if not l1 or not l2:
#     print(l1 or l2)


# t1 = 't1'
# t1 = 10
# t1 = None
# t2 = 't2'
# t2 = None
# t2 = 20
# print(t1 and t2)


# 7,2,6,1,4


# for i in range(2,5):
#     print(i)


# t = 15
# t = 8
# rel = bin(t)
# print(type(rel),rel)


# s = Solution()
# print(s.isHappy(2))
# print(np.sqrt(np.array([int(n) for n in str(2)])))

# h_num = 2
# print([int(n) for n in str(h_num)])



# t = 35
# str(t)


# t = 35
# for i in t:
#     print(i)

# t = []
# print(min(t))
# [2,4,1]
#
# [7,1,5,3,6,4]

# t = [1,2,3,4]
# rel = t.index(3)
# print(rel)


# t = [1,2,3,4]
# rel = t.pop(2)
# print(rel)
# print(t)


# print(10/2)# 5.0
# print(10//2)# 5
# print(10.5/2)# 5.25
# print(7//3)# 2
# # print(10.5//2)# 5.0
# print(1//2)# 0
# print(2//2)# 1


# t1 = [1,2,1,2,3]
# t2 = [2,3,2,4]
# rel1 = Counter(t1)
# rel2 = Counter(t2)
#
# print(list(rel1.elements()))# [1, 1, 2, 2, 3]
# print(type(rel1.most_common()),rel1.most_common())
# # <class 'list'> [(1, 2), (2, 2), (3, 1)]
#
# print(rel1)# Counter({1: 2, 2: 2, 3: 1})
# print(rel2)# Counter({2: 2, 3: 1, 4: 1})
# # Counter类的+, -, &, |操作
# rst = rel1 & rel2# 求交集
# print(rst)# Counter({2: 2, 3: 1})
# rst = rel1 | rel2# 求并集
# print(rst)# Counter({1: 2, 2: 2, 3: 1, 4: 1})
# rst = rel1 + rel2
# print(rst)# Counter({2: 4, 1: 2, 3: 2, 4: 1})
# rst = rel1 - rel2
# print(rst)# Counter({1: 2})





# t = '您好，我们一行4位成人，1位儿童和1位2岁以下幼儿，过来旅游，想要预订03月26日-03月27日的房，共1天。请问这个时间方便接待吗？ '
# if '旅游' in t:
#     print('zai')


# n = 432

# rel = max(1,3)
# print(rel)


# dic = {1:1,2:2}
# for k,v in dic.items():
#     if v==1:
#         print(k)
#

# print(1 in dic)


# def t(nums):
#     dic = {}
#     for n in nums:
#         if n not in dic:
#             dic[n] = 1
#             continue
#         dic[n] += 1
#     print(dic)
#     for k, v in dic.items():
#         if v == 1:
#             return k
#
# print(t([1]))



# t = [1,2,4,2,1,6,6]
# rel = t.remove(5)
# print(rel)
# print(t)



# dic = {}
# rel1 = dic.setdefault(1,'a')
# rel2 = dic.setdefault(1,'c')
# print(rel1) #a
# print(rel2) #a



# l = [1,2,3,4,3]
#
# l.pop(0)
# l.pop()
# print(l)

# dque = deque(l)
# dque.appendleft(1)
# dque.popleft()
# print(dque)
# print(type(dque),'---',dque)
# for d in dque:
#     print(d)

# rel = l.count(3)
# print(type(rel),rel)
# l.remove(3)
# print(l)
# rel = l.pop()
# print(rel)
# print(l)

# stack
# l.append()
# l.pop()

# queue
