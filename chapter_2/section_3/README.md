### 2. 实现Singleton模式

使用`__new__`控制实例创建过程

```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    pass
```
使用decorator

```python
from functools import wraps
def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance

@singleton
class Myclass:
    pass
```

使用元类

```python
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
        
    def __call__(self, *args, **kwargs): 
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance 
        else:
            return self.__instance
# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')
```

### 3 数组中重复的数字

#### [牛客网传送门](https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)

书中参数还传了一个数组用来保存重复的数字，身为一个Pythoner，直接返回tuple。

```python
def duplicate(nums: list) -> int:
    for i, num in enumerate(nums):
        while i != num:
            if num == nums[num]:
                return True, num
            else:
                nums[i], nums[num] = nums[num], nums[i]
                num = nums[i]
    return False, None
```

### 3_1 数组中重复的数字，不能修改数组

#### [AcWing传送门](https://www.acwing.com/problem/content/15/)

元素范围变成了1~n。此方法有缺陷，不能找出所有的重复的数字，因为在1~2的范围里有1和2两个数字，这个范围的数字也出现两次，不能确定是每个数字各出现一次还是某个数字出现了两次。

```python
def find_duplicate(nums: list) -> int:
    def count_range(i, j):
        return sum(i<=num<=j for num in nums)

    lo = 1
    hi = len(nums) - 1     # n为范围
    while lo <= hi:
        mid = (lo + hi) // 2
        count = count_range(lo, mid)
        if lo == hi:
            if count > 1:
                return lo
            else:
                break
        if count > mid-lo+1:
            hi = mid
        else:
            lo = mid + 1
    return -1
```

### 4 二维数组中的查找

#### [牛客网传送门](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

#### [LeetCode传送门](<https://leetcode.com/problems/search-a-2d-matrix-ii/>)

选取右上角为起始点。

```python
def find(target, array):
    row = 0
    col = len(array[0]) - 1
    while col >= 0 and row <= len(array)-1:
        if array[row][col] > target:
            col -= 1
        elif array[row][col] < target:
            row += 1
        else:
            return True
    return False
```

更为优雅的方法。

```python
def searchMatrix(self, matrix, target):
    j = -1
    for row in matrix:
        while j + len(row) and row[j] > target:
            j -= 1
        if row[j] == target:
            return True
    return False
```

### 5 替换空格

#### [牛客网传送门](https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

```python
def replaceSpace(self, s):
    return ''.join(c if c!=' ' else '%20' for c in s)
```

### 6 从尾到头打印链表

#### [牛客网传送门](https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

```python
def printListFromTailToHead(self, listNode):
    stack, h = [], listNode
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]
```

### 7 重建二叉树

#### [LeetCode传送门](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

说明：根据前序遍历和中序遍历重建二叉树，假设遍历结果中不包含重复的数字。
```python
def buildTree(preorder, inorder):
    if preorder == []:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    cut = inorder.index(root_val)
    root.left = buildTree(preorder[1:cut+1], inorder[:cut])
    root.right = buildTree(preorder[cut+1:], inorder[cut+1:])
    return root
```
方法二：空间复杂度更低的解法。

```python
def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)
```

### 8 二叉树的下一个节点

#### [牛客网传送门](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=3)

```python
def GetNext(self, pNode):
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
```

### 9 用两个栈实现队列

#### [LeetCode传送门](https://leetcode.com/problems/implement-queue-using-stacks/description/)

```python
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        
    def pop(self) -> int:
        return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1[-1]
        
    def empty(self) -> bool:
        return self.s1 == []
```

### 9_1 用两个队列实现栈

#### [LeetCode传送门](https://leetcode.com/problems/implement-stack-using-queues/description/)

两个队列
```python
class MyStack:

    def __init__(self):
        from collections import deque
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return not self.q1

```
单队列旋转
```python
class MyStack:

    def __init__(self):
        from collections import deque
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # self.q.rotate(1)  这里是用了双端队列的特性
        # self.q.rotate(1-len(self.q))  这里和下面循环是一样的效果
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return not self.q
```
