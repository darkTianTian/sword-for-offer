#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 2:35 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    从尾到头打印链表。
    >>> l1 = (1, 2, 3, 4, 5)
    >>> l1 = construct_linklist(l1)
    >>> print_list_reverse(l1)
    [5, 4, 3, 2, 1]
    >>> l2 = construct_linklist([3, 4, 8, 2, 7])
    >>> print_list_reverse(l2)
    [7, 2, 8, 4, 3]
"""
from utils import construct_linklist, ListNode


def print_list_reverse(head: ListNode) -> list:
    stack, h = [], head
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]