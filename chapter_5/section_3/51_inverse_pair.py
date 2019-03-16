#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:41 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    数组中的逆序对
    >>> InversePairs([7, 5, 6, 4])
    5
"""

from collections import deque


def InversePairs(data: list) -> int:
    count = 0

    def merge(left, right):
        nonlocal count
        q = deque()             # 双端队列是为了更快地从头取出
        l, r = len(left) - 1, len(right) - 1
        while l >= 0 and r >= 0:
            if left[l] > right[r]:
                count += r + 1
                q.appendleft(left[l])
                l -= 1
            else:
                q.appendleft(right[r])
                r -= 1
        # q.extendleft(left[l:-1:-1] or right[r:-1:-1])
        q = left[:l + 1] + right[:r + 1] + list(q)
        return q

    def merge_sort(ary: list):
        if len(ary) <= 1: return ary
        mid = len(ary) // 2
        left = merge_sort(ary[:mid])
        right = merge_sort(ary[mid:])
        return merge(left, right)

    merge_sort(data)
    return count % 1000000007