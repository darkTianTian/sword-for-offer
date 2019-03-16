#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/10 10:12 AM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    二叉搜索树转双向链表
    >>> t_str = '10,6,4,$,$,8,$,$,14,12,$,$,16,$,$'
    >>> t1 = deserialize_tree(t_str)
    >>> correct = inorder_traversal(t1)
    >>> correct
    [4, 6, 8, 10, 12, 14, 16]

    # test first
    >>> ans = convert(t1)
    >>> check_ans(ans, correct)
    True

    # test second
    >>> t1 = deserialize_tree(t_str)
    >>> ans2 = convert2(t1)
    >>> check_ans(ans, correct)
    True

    # test third
    >>> t1 = deserialize_tree(t_str)
    >>> ans2 = convert3(t1)
    >>> check_ans(ans, correct)
    True

"""

from utils import deserialize_tree, inorder_traversal

def convert(root: 'TreeNode') -> 'TreeNode':
    """
    解法1：遍历两次。
    """
    if not root:
        return None
    inorder = []
    def dfs(node):
        if node:
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)

    dfs(root)
    for i, n in enumerate(inorder[:-1]):
        n.right = inorder[i+1]
        inorder[i+1].left = n
    return inorder[0]


def convert2(root: 'TreeNode') -> 'TreeNode':
    """
    解法2：递归。
    """
    def convert_tree(node):
        if not node:
            return None
        if node.left:
            left = convert_tree(node.left)
            while left.right:
                left = left.right
            left.right = node
            node.left = left
        if node.right:
            right = convert_tree(node.right)
            while right.left:
                right = right.left
            right.left = node
            node.right = right
        return node

    if not root:
        return root
    root = convert_tree(root)
    while root.left:
        root = root.left
    return root

def convert3(root: 'TreeNode') -> 'TreeNode':
    """
    解法3：Morris Traversal.
    """
    cur = root
    pre = ans = None
    while cur:
        while cur.left:
            q = cur.left
            while q.right:
                q = q.right
            q.right = cur                   # 补齐右指针
            cur.left, cur = None, cur.left  # 拆掉左指针
        cur.left = pre
        if pre is None:
            ans = cur   # 这里是为了找到链表的头，只执行一次
        else:
            pre.right = cur
        pre, cur = cur, cur.right
    return ans

def check_ans(root: 'TreeNode', right) -> 'bool':
    asc, desc = [], []
    pre = None
    while root:
        asc.append(root.val)
        pre, root = root, root.right

    while pre:
        desc.append(pre.val)
        pre = pre.left
    desc.reverse()
    return asc==right==desc