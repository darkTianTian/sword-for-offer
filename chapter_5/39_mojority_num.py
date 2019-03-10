#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 4:56 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    数组中超过一半的数。
    >>> nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    >>> majority_element(nums)
    2
    >>> majority_element2(nums)
    2
    >>> majority_element3(nums)
    2

"""

# 牛客网中把此题改了，这个超过一半的数可能不存在，这样就没法用波义尔摩尔投票的经典解法了。
# 我们不管它，按照书中的解法为准。


def majority_element(nums: 'List[int]') -> int:
    """
    解法1：排序。
    """
    return sorted(nums)[len(nums)//2]

def majority_element2(nums: 'List[int]') -> int:
    """
    解法2：使用Counter.
    """
    from collections import Counter
    c = Counter(nums)
    # return max(c.keys(), key=c.get)
    return c.most_common(1)[0][0]

def majority_element3(nums: 'List[int]') -> int:
    """
    解法3：波义尔摩尔投票法。
    """
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate