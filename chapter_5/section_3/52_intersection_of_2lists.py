#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 5:45 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    两个链表的第一个公共节点。
    >>> h1 = construct_linklist([4, 2, 1, 5, 5, 7])
    >>> h2 = construct_linklist([8, 3])
    >>> h2.next.next= h1.next.next
    >>> intersection = h1.next.next
    >>> intersection is getIntersectionNode(h1, h2)
    True

"""

from utils import construct_linklist

def getIntersectionNode(headA: 'ListNode', headB: 'ListNode') -> 'ListNode':
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1
