### 2. 实现Singleton模式

#### 使用`__new__`控制实例创建过程

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
#### 使用decorator

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

#### 使用元类
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

### 4 二维数组中的查找

#### 选取右上角为起始点。

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

### 5 替换空格

```python
def replaceSpace(self, s):
    return ''.join(c if c!=' ' else '%20' for c in s)
```

### 6 从尾到头打印链表

```python
def printListFromTailToHead(self, listNode):
    stack, h = [], listNode
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]
```

### 7 重建二叉树
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

### 9 用两个栈实现队列

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
