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
        # write code here
    visited = [[False] * cols for _ in range(rows)]

    def get_sum(x, y):
        return sum(map(int, str(x) + str(y)))

    def movingCore(threshold, rows, cols, i, j):
        if get_sum(i, j) <= threshold:
            visited[i][j] = True
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
                    movingCore(threshold, rows, cols, x, y)

    movingCore(threshold, rows, cols, 0, 0)
    return sum(sum(visited, []))