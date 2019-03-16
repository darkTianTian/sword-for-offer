#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 7:04 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    反转链表。
    >>> h1 = construct_linklist([1, 2, 3, 4, 5])
    >>> print(pretty_linklist(h1))
    1->2->3->4->5
    >>> h2 = reverse_list(h1)
    >>> print(pretty_linklist(h2))
    5->4->3->2->1
"""

from utils import construct_linklist, pretty_linklist

def reverse_list(head: 'ListNode') -> 'ListNode':
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev