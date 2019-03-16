#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 10:58 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    根据入栈和出栈顺序，判断是否能够清空该栈。
    >>> pushed = [1, 2, 3, 4, 5]
    >>> popped = [4, 5, 3, 2, 1]
    >>> validateStackSequences(pushed, popped)
    True
    >>> validateStackSequences(pushed, [4, 3, 5, 1, 2])
    False
"""

def validateStackSequences(pushed: 'List[int]', popped: 'List[int]') -> 'bool':
    stack = []
    j = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)