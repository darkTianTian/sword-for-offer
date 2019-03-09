#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 8:27 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


"""
    序列化反序列化二叉树。

"""

from utils import TreeNode

def serialize_tree(root):
    if not root:
        return '$'
    return (str(root.val) + ',' + serialize_tree(root.left) +
            ',' + serialize_tree(root.right))

def deserialize_tree(data):
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