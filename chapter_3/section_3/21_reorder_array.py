#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 5:40 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    调整数组顺序使奇数位于偶数面前

    >>> ary = list(range(15))
    >>> random.shuffle(ary)
    >>> reorder_array(ary)
    >>> check_odd_even(ary) and sorted(ary)==sorted(list(range(15)))
    True

    # test second
    >>> random.shuffle(ary)
    >>> ary2 = reorder_array2(ary)
    >>> check_odd_even(ary2) and sorted(ary2) == sorted(list(range(15)))
    True

    # test third
    >>> random.shuffle(ary)
    >>> ary3 = reorder_array3(ary)
    >>> check_odd_even(ary3) and sorted(ary3)==sorted(list(range(15)))
    True
"""

import random
from collections import deque
from itertools import dropwhile


### 这道题在牛客网上有些不一样，牛客网要求奇偶的相对位置不变，所以解法1不能通过牛客网测试。
### 但是解法1却是时间和空间复杂度最优解。

def reorder_array(array: 'List[int]') -> 'List[int]':
    """
    解法1：双指针。Time: O(n), Space: O(1)
    """
    l, r = 0, len(array)-1
    while l < r:
        while l < r and array[l]&1 == 1:
            l += 1
        while l < r and array[r]&1 == 0:
            r -= 1
        array[l], array[r] = array[r], array[l]

def reorder_array2(array: 'List[int]') -> 'List[int]':
    """
    解法2：排序。Time: O(nlogn), Space: O(1)
    """
    return sorted(array, key=lambda x:x&1==0)

def reorder_array3(array: 'List[int]') -> 'List[int]':
    """
    解法3：双端队列插入，Time: O(n), Space: O(n)
    """
    q = deque()
    n = len(array)
    for i in range(n):
        if array[-i-1] & 1 == 1:  # 从后找奇数
            q.appendleft(array[-i-1])
        if array[i] & 1 == 0:  #从前找偶数
            q.append(array[i])
    return q


def check_odd_even(ary: 'List[int]') -> 'bool':
    return all(n&1==0 for n in dropwhile(lambda x: x&1==1, ary))
