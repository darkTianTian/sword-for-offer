#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 6:59 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    二叉树的深度。
    >>> t1 = '1,2,4,$,$,5,7,$,$,$,3,$,6,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> max_depth(t1)
    4
    >>> max_depth2(t1)
    4
"""

from collections import deque

from utils import deserialize_tree


def max_depth(root: 'TreeNode') -> int:
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

def max_depth2(root: 'TreeNode') -> 'int':
    q = root and deque([(root, 1)])
    d = 0
    while q:
        node, d = q.popleft()
        if node.right:
            q.append((node.right, d+1))
        if node.left:
            q.append((node.left, d+1))
    return d