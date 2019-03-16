#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 10:40 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    顺时针打印矩阵
    >>> m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> spiral_order(m)
    [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    >>> m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> anti_clock_wise(m)
    [1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2, 6, 10, 11, 7]
    >>> anti_clock_wise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 4, 7, 8, 9, 6, 3, 2, 5]
"""

#   这是我最喜欢的写法了，原创来自LeetCode一位大神，
#   相信如果你经常刷LeetCode，应该知道我说的是谁

def spiral_order(matrix: 'List[List[int]]') -> list:
    return (matrix and list(matrix.pop(0)) +
            spiral_order(list(zip(*matrix))[::-1]))


# 下面为一个变种，逆时针打印。

def anti_clock_wise(matrix: 'List[List[int]]') -> list:
    if not matrix:
        return []
    clock_wise = list(zip(*(matrix[::-1])))
    a = list(clock_wise.pop(0))[::-1]
    b = anti_clock_wise(clock_wise)
    return a + b