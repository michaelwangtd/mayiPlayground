#/usr/bin python
# -*- coding:utf-8 -*-

# longest common prefix
# str_list = ['abc','abdda','abttd']

def longest_common_prefix(strs):
    comfix = ''
    if strs:
        mix_len = len(strs[0])
        for str_item in strs:
            if len(str_item)<mix_len:
                mix_len = len(str_item)
    else:return comfix
    if mix_len>0:
        for i in range(mix_len):
            item_prefix = strs[0][i]
            flag = True
            for str_item in strs:
                if str_item[i] != item_prefix:
                    flag = False
                    break
            if flag:
                comfix += item_prefix
            else:break
        return comfix
    else:return comfix


# palindrome number
def palindrome(integer):
    if isinstance(integer,int):
        if integer<0:
            return False
        cake = str(integer)
        i = 0
        j = len(cake)-1
        while i<=j:
            if cake[i]!=cake[j]:
                return False
            i += 1
            j -= 1
        return True

# roman2integer
def roman2int(s):
    '''
    "DCXXI"
    :return:
    '''
    trans_dic =  {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i,v in enumerate(s):
        if i==len(s)-1 or trans_dic[s[i]] > trans_dic[s[i+1]]:
            result += trans_dic[s[i]]
        else:
            result -= trans_dic[s[i]]
    return result

# is valid parentheses
def is_valid_parentheses(s):
    '''
    "["
    "[)"
    "([])"
    "(])"
    :param s:
    :return:
    '''
    dic = {')':'(' , '}':'{' , ']':'[' }
    l_list = ['(','[','{']
    stack = []
    for i, v in enumerate(s):
        if v in l_list:
            stack.append(v)
        else:
            if not stack:
                return False
            if dic[v] == stack[-1]:
                stack.pop()
            else:
                return False
    return False if stack else True

# merge two linked list
class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None

def mergeTwoLists(l1,l2):
    '''

    :param l1:ListNode
    :param l2:ListNode
    :return: l:ListNode
    '''






def orderSortestSubArr(arr):
    '''
    arr = [2, 6, 4, 8, 10, 9, 15]
    arr = [1,2,3,4,5,2]
    arr = [1,2,2,3,4,5]
    arr = [1,6,2,3,4,8]
    arr = [1,2,3,4,6,8]
    arr = [1]
    :return:
    '''
    if not arr:
        return False
    i = 0
    j = len(arr)-1
    while i<=j:
        if i==j:
            return 0
        if i+1<len(arr) and arr[i]<=arr[i+1]:
            i += 1



def isDuplicate(arr):
    cake = list(set(arr))
    return True if len(arr)==len(cake) else False





def isOneBitCharacterEndWith(bits):
    '''
    [1,0,0]
    [1, 1, 1, 1, 0]
    :param bits:
    :return:
    '''



















if __name__ == '__main__':
    pass