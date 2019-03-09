#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 10:12 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    二叉树的镜像
    >>> t1 = '8,6,5,$,$,7,$,$,10,9,$,$,11,$,$'
    >>> t2 = '8,10,11,$,$,9,$,$,6,7,$,$,5,$,$'
    >>> t1 = deserialize_tree(t1)
    >>> t2 = deserialize_tree(t2)
    >>> mirror(t1)
    >>> is_same_tree(t1, t2)
    True

"""

from utils import deserialize_tree, TreeNode, is_same_tree


def mirror(root: TreeNode):
    if root:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)