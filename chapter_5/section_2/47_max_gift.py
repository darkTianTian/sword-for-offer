#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/18 2:35 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    礼物的最大价值
    >>> m = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    >>> get_max_value(m)
    53
"""
import itertools


def get_max_value(g: 'List[List[int]]') -> int:
    R, C = len(g), len(g[0])
    cur = list(itertools.accumulate(g[0]))
    for i in range(1, R):
        tmp = []
        for j in range(C):
            left = tmp[-1] if j > 0 else float('-inf')
            tmp.append(max(cur[j], left) + g[i][j])
        cur = tmp
    return cur[-1]