#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 6:48 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    链表中倒数第k个节点
    >>> l1 = construct_linklist([1, 2, 3, 4, 5])
    >>> find_kth_to_tail(l1, 3) is l1.next.next
    True
    >>> find_kth_to_tail(l1, 7)
    >>> find_kth_to_tail(l1, 1) is l1.next.next.next.next
    True

"""

from utils import construct_linklist

def find_kth_to_tail(head: 'ListNode', k: int) -> 'ListNode':
    fast = slow = head
    for _ in range(k):
        if fast:
            fast = fast.next
        else:
            return None
    while fast:
        slow, fast = slow.next, fast.next
    return slow