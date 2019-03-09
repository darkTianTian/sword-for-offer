#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 6:57 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    链表中环的入口节点
    >>> h1 = construct_linklist([1, 2, 3, 4, 5, 6])
    >>> h1.next.next.next.next.next.next = h1.next.next
    >>> detect_cycle(h1) is h1.next.next
    True

"""

from utils import  construct_linklist


def detect_cycle(head: 'ListNode') -> 'ListNode':
    fast = slow = head
    # 检测是否有环
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
    else:
        return None
    # 找出入口节点
    h = head
    while h is not slow:
        h, slow = h.next, slow.next
    return h