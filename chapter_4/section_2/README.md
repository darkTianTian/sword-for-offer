### 27 二叉树的镜像

#### [牛客网传送门](https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011?tpId=13&tqId=11171&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

#### [AcWing传送门](https://www.acwing.com/problem/content/37/)


```python
def Mirror(self, root):
    if root:
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
```

迭代

```python
def Mirror(self, root):
    stack = root and [root]
    while stack:
        n = stack.pop()
        if n:
            n.left, n.right = n.right, n.left
            stack += n.right, n.left
```
### 28 对称的二叉树

#### [LeetCode传送门](https://leetcode.com/problems/symmetric-tree/description/)

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

方法一：recursively.

```python
def isSymmetric(self, root: 'TreeNode') -> 'bool':

    def symmetric(p1, p2):
        if p1 and p2:
            return (p1.val == p2.val and symmetric(p1.left, p2.right) and 
                    symmetric(p1.right, p2.left))
        else:
            return p1 is p2

    if not root:
        return True
    return symmetric(root.left, root.right)
```

方法二：iteratively.

```python
def isSymmetric(self, root: 'TreeNode') -> 'bool':
    stack = root and [(root.left, root.right)]        
    while stack:
        p1, p2 = stack.pop()
        if not p1 and not p2: continue
        if not p1 or not p2: return False
        if p1.val != p2.val: return False
        stack.append((p1.left, p2.right))
        stack.append((p1.right, p2.left))
    return True
```

### 29 顺时针打印矩阵

#### [LeetCode传送门](https://leetcode.com/problems/spiral-matrix/description/)

这里注意一点`matrix.pop(0)`需要转成list，因为zip函数中的每个元素是一个tuple，如果不转变成了一个`tuple+list`，会抛出异常。

```python
def spiralOrder(self, matrix):
    return (matrix and list(matrix.pop(0)) + 
            self.spiralOrder(list(zip(*matrix))[::-1]))
```

此题有个变形，如果逆时针该如何打印。这样的话情况稍微复杂一些。

```python
def anti_clock_wise(self, matrix)
    if not matrix:
        return []
    clock_wise = list(zip(*(matrix[::-1])))
    a = list(clock_wise.pop(0))[::-1]
    b = self.anti_clock_wise(clock_wise)
    return a + b
```