#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 10:55 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    在O(1)时间复杂度获得最小值得栈。
    >>> ms = MinStack()
    >>> ms.push(-2)
    >>> ms.push(0)
    >>> ms.push(-3)
    >>> ms.getMin()
    -3
    >>> ms.pop()
    >>> ms.top()
    0
    >>> ms.getMin()
    -2
"""


class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if x < cur_min:
            cur_min = x
        self._stack.append((x, cur_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        if not self._stack:
            return None
        else:
            return self._stack[-1][0]

    def getMin(self) -> int:
        if not self._stack:
            return float('inf')
        else:
            return self._stack[-1][1]