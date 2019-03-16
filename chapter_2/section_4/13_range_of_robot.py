#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 4:26 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    机器人的运动范围
    >>> movingCount(2, 3, 4)
    6
"""


def movingCount(threshold: int, rows: int, cols: int) -> int:
    def get_sum(x, y):
        return sum(map(int, str(x))) + sum(map(int, str(y)))

    def movingCountCore(threshold, rows, cols, i, j):
        if get_sum(i, j) <= threshold:
            visited[i * cols + j] = True
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (0 <= x < rows and 0 <= y < cols and
                        not visited[x * cols + y]):
                    movingCountCore(threshold, rows, cols, x, y)

    visited = [False] * rows * cols
    movingCountCore(threshold, rows, cols, 0, 0)
    return sum(visited)