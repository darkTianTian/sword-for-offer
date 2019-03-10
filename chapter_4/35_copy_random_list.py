#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 11:33 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    复杂链表的复制。
    >>> n1, n2, n3 = RandomListNode(1), RandomListNode(2), RandomListNode(3)
    >>> n4, n5 = RandomListNode(4), RandomListNode(5)
    >>> n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    >>> n3.random, n2.random = n1, n5
    >>> print(pretty_linklist(n1))
    1->2->3->4->5
    >>> head2 = copyRandomList2(n1)
    >>> print(pretty_linklist(head2))
    1->2->3->4->5
    >>> check_same(n1, head2)
    True
    >>> head3 = copyRandomList(n1)
    >>> check_same(n1, head3)
    True
    >>> n3.random = n3
    >>> check_same(n1, head3)
    False
    >>> check_same(n1, head2)
    False
    >>> check_same(head2, head3)
    True
"""

from utils import ListNode, pretty_linklist

class RandomListNode(ListNode):

    def __init__(self, x):
        super().__init__(x)
        self.random = None


def copyRandomList(head: 'RandomListNode') -> 'RandomListNode':
    """
    解法1：遍历两次
    """
    cp_map = {}

    m = n = head
    while m:
        cp_map[m] = RandomListNode(m.val)
        m = m.next
    while n:
        cp_map[n].next = cp_map.get(n.next)
        cp_map[n].random = cp_map.get(n.random)
        n = n.next

    return cp_map.get(head)

def copyRandomList2(head: 'RandomListNode') -> 'RandomListNode':
    """
    解法2：遍历一次
    """
    from collections import defaultdict
    cp = defaultdict(lambda: RandomListNode(0))
    cp[None] = None
    n = head
    while n:
        cp[n].val = n.val
        cp[n].next = cp[n.next]
        cp[n].random = cp[n.random]
        n = n.next
    return cp[head]

def check_same(h1, h2):
    n1, n2 = h1, h2
    while n1 and n2:
        if n1.val != n2.val:
            return False
        if n1.random and n2.random:
            if n1.random.val != n2.random.val:
                return False
        elif n1.random is not n2.random:
            return False
        n1, n2 = n1.next, n2.next
    return n1 is n2