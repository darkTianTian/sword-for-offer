#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/17 6:01 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    验证后序遍历是否是某个二叉搜索树的遍历结果。

    >>> verify_sequence([5, 7, 6, 9, 11, 10, 8])
    True
    >>> verify_sequence([4,6,7,5])
    True
    >>> verify_sequence([7, 4, 6, 5])
    False

"""
from itertools import takewhile, dropwhile

def verify_sequence(seq: list) -> 'bool':

    if not seq:
        return False
    p = seq[-1]
    left_sub = list(takewhile(lambda x: x < p, seq[:-1]))
    right_sub = seq[len(left_sub):-1]
    if not all(x>p for x in right_sub):
        return False
    left = right = True
    if left_sub:
        left = verify_sequence(left_sub)
    if right_sub:
        right = verify_sequence(right_sub)
    return left and right