#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/9 3:03 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com

"""
    根据前序遍历和中序遍历重建二叉树。
    >>> preorder = [3, 9, 20, 15, 7]
    >>> inorder = [9, 3, 15, 20, 7]
    >>> t1 = buildTree(preorder, inorder)
    >>> preorder_traversal(t1) == preorder
    True
    >>> inorder_traversal(t1) == inorder
    True

    # test t2
    >>> t2 = buildTree2(preorder, inorder)
    >>> preorder_traversal(t2) == preorder
    True
    >>> inorder_traversal(t2) == inorder
    True
"""

from utils import TreeNode, preorder_traversal, inorder_traversal

def buildTree(preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
    """
    解法1：解法一有个问题，在一个极端情况下，例如前序遍历为[1, 2, 3, 4, 5]
    中序遍历为[5, 4, 3, 2, 1]，这种情况只有左子树，那么在中序遍历使用index寻找根节点时，
    时间复杂度为O(n²)
    """
    if preorder == []:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    cut = inorder.index(root_val)
    root.left = buildTree(preorder[1:cut+1], inorder[:cut])
    root.right = buildTree(preorder[cut+1:], inorder[cut+1:])
    return root


def buildTree2(preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
    """
    解法2：解决上述为题，并且没有多余的切片产生的内存，空间复杂度也更小了。
    """
    preo, inor = list(preorder), list(inorder)
    def build(stop):
        if inor and inor[-1] != stop:
            root = TreeNode(preo.pop())
            root.left = build(root.val)
            inor.pop()
            root.right = build(stop)
            return root
    preo.reverse()
    inor.reverse()
    return build(None)

