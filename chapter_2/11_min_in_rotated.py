#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 4:13 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    在一个排序数组旋转后的结果中，找出最小元素。
    >>> find_min([3, 4, 5, 1, 2])
    1
    >>> find_min([3, 4, 5, 0, 1, 2])
    0
"""

def find_min(nums: 'List[int]') -> int:
    l, r = 0, len(nums)-1
    if nums[l] < nums[r]:  #  此时升序，直接返回
        return nums[l]
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] > nums[l]:
            l = mid
        elif nums[mid] < nums[r]:
            r = mid
        else:
            return nums[r]