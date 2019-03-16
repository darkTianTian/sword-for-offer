#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 5:17 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    删除链表中的节点，给定的节点不是尾节点。
    >>> head = construct_linklist([1, 2, 3, 4, 9])
    >>> print(pretty_linklist(head))
    1->2->3->4->9
    >>> to_del = head.next.next
    >>> delete_node(to_del)
    >>> print(pretty_linklist(head))
    1->2->4->9
"""

from utils import construct_linklist, pretty_linklist

def delete_node(node: 'ListNode'):
    node.val = node.next.val
    node.next = node.next.next