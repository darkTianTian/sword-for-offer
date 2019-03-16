#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 3:46 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    两个队列实现栈。
    # test s1
    >>> s1 = MyStack()
    >>> s1.push(1)
    >>> s1.push(2)
    >>> s1.top()
    2
    >>> s1.pop()
    2
    >>> s1.top()
    1

    # test s2
    >>> s2 = MyStack2()
    >>> s2.push(1)
    >>> s2.push(2)
    >>> s2.top()
    2
    >>> s2.pop()
    2
    >>> s2.pop()
    1
    >>> s2.empty()
    True
"""

from collections import deque


class MyStack:
    """
    解法1：push:O(n), pop/top:O(1).
    """
    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


class MyStack2:
    """
    解法2： 队列旋转。
    """
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # self.q.rotate(1)  这里是用了双端队列的特性，所以这么写是不符合题意的。
        # self.q.rotate(1-len(self.q))  这里和下面循环是一样的效果
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q