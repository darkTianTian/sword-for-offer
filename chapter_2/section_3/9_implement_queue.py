#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 3:28 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    用两个栈实现队列

    test 1
    >>> q1 = MyQueue1()
    >>> q1.push(1)
    >>> q1.push(2)
    >>> q1.peek()
    1
    >>> q1.pop()
    1
    >>> q1.empty()
    False

    # test q2
    >>> q2 = MyQueue2()
    >>> q2.push(1)
    >>> q2.push(3)
    >>> q2.peek()
    1
    >>> q2.pop()
    1
    >>> q2.peek()
    3
    >>> q2.empty()
    False
    >>> q2.pop()
    3
"""


class MyQueue1:
    """
    push: O(1), pop/peek: O(n)
    使用一个入栈用来接收数据，使用一个出栈用来返回数据。
    """
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def move(self) -> None:
        if self.out_stack == []:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return self.in_stack == self.out_stack == []


class MyQueue2:
    """
    push: O(n), pop/peek: O(1)
    """
    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1