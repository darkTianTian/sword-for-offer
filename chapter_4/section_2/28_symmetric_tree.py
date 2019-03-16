#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 10:33 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    对称的二叉树
    >>> t1 = '8,6,5,$,$,7,$,$,6,7,$,$,5,$,$'
    >>> t2 = '8,6,5,$,$,7,$,$,9,7,$,$,5,$,$'
    >>> t3 = '7,7,7,$,$,7,$,$,7,7,$,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> t2 = deserialize_tree(t2)
    >>> t3 = deserialize_tree(t3)
    >>> isSymmetric(t1)
    True
    >>> isSymmetric(t2)
    False
    >>> isSymmetric(t3)
    False
"""

from utils import deserialize_tree

def isSymmetric(root: 'TreeNode') -> 'bool':

    def symmetric(p1, p2):
        if p1 and p2:
            return (p1.val == p2.val and symmetric(p1.left, p2.right) and
                    symmetric(p1.right, p2.left))
        else:
            return p1 is p2

    if not root:
        return True
    return symmetric(root.left, root.right)