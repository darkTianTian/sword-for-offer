#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/16 10:20 PM
# @Author   : xiaoliji
# @Email    : yutian9527@gmail.com


def GetNext(pNode):
    # write code here
    if not pNode:
        return None
    # 有右子树，右子树中最左节点
    if pNode.right:
        pre = pNode.right
        while pre.left:
            pre = pre.left
        return pre
    while pNode.next:
        parent = pNode.next
        if parent.left == pNode:
            return parent
        pNode = parent
    return None