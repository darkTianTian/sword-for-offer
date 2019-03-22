#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 4:19 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    矩阵中的路径
    >>> hasPath('ABEESFCSADME', rows=3, cols=4, path='SEE')
    True
    >>> hasPath('abtgcfcsjdeh', rows=3, cols=4, path='bfce')
    True
    >>> hasPath('abtgcfcsjdeh', rows=3, cols=4, path='abfb')
    False
    >>> hasPath('ABCESFCSADEE', rows=3, cols=4, path='SEE')
    True
    >>> hasPath('ABCESFCSADEE', rows=3, cols=4, path='ABCESEEEFS')
    True
"""



def hasPath(matrix: str, rows: int, cols: int, path: str) -> 'bool':
    """
    回溯法，此题牛客网中的testcase不全，排行榜的答案不一定是正确的。
    如doctest中的第一个示例，应该是True，但如果返回False，也能通过牛客网的测试用例。
    """
    for i in range(rows):
        for j in range(cols):
            if matrix[i * cols + j] == path[0]:
                if spread(list(matrix), rows, cols, path[1:], i, j):
                    return True
    return False


def spread(matrix: str, rows: int, cols: int, path: str, i: int, j: int) -> 'bool':
    if not path:
        return True
    matrix[i * cols + j] = '-'
    spreaded = False
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= x < rows and 0 <= y < cols and matrix[x * cols + y] == path[0]:
            if spread(matrix, rows, cols, path[1:], x, y):
                spreaded = True
    return spreaded