#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 7:10 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    合并两个有序链表。
    >>> h1 = construct_linklist([1, 2, 4])
    >>> h2 = construct_linklist([1, 3, 4])
    >>> print(pretty_linklist(mergeTwoLists(h1, h2)))
    1->1->2->3->4->4

    >>> h1 = construct_linklist([1, 2, 4])
    >>> h2 = construct_linklist([1, 3, 4])
    >>> print(pretty_linklist(mergeTwoLists2(h1, h2)))
    1->1->2->3->4->4
"""

from utils import ListNode, construct_linklist, pretty_linklist


def mergeTwoLists(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    """
    解法1：迭代。
    """
    l = head = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            l.next, l1 = l1, l1.next
        else:
            l.next, l2 = l2, l2.next
        l = l.next
    l.next = l1 or l2
    return head.next


def mergeTwoLists2(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    """
    解法2：递归。
    """
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2