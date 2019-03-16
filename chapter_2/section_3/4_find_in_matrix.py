#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 1:30 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    在从左到右从上到下递增的矩阵中，判断目标数是否存在

    >>> m = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    >>> search_in_matrix(7, m)
    True
    >>> search_in_matrix(5, m)
    False
"""

# 思路：从右上角顶点出发。

def search_in_matrix(target: int, matrix: 'List[List[int]]') -> 'bool':

    row = 0
    col = len(matrix[0]) - 1
    while col >= 0 and row <= len(matrix) - 1:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    return False


