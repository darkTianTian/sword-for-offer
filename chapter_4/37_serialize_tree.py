#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 8:27 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    序列化反序列化二叉树。
    >>> t1 = TreeNode(1)
    >>> t1.left, t1.right = TreeNode(2), TreeNode(3)
    >>> t1.left.left, t1.right.left, t1.right.right = TreeNode(4), TreeNode(5), TreeNode(6)
    >>> t2 = copy.copy(t1)
    >>> t3_str =  serialize_tree(t1)
    >>> t3 = deserialize_tree(t3_str)
    >>> is_same_tree(t2, t3)
    True

"""

import copy
from utils import TreeNode, is_same_tree

def serialize_tree(root: 'TreeNode') -> str:
    if not root:
        return '$'
    return (str(root.val) + ',' + serialize_tree(root.left) +
            ',' + serialize_tree(root.right))

def deserialize_tree(data: str) -> 'TreeNode':
    nodes = data.split(',')[::-1]
    return deserialize_tree_util(nodes)

def deserialize_tree_util(nodes):
    val = nodes.pop()
    if val == '$':
        return None
    root = TreeNode(int(val))
    root.left = deserialize_tree_util(nodes)
    root.right = deserialize_tree_util(nodes)
    return root