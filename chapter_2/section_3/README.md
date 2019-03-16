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

### 4.二维数组中的查找

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

### 5.替换空格

```python
def replaceSpace(self, s):
    return ''.join(c if c!=' ' else '%20' for c in s)
```

### 6.从尾到头打印链表

```python
def printListFromTailToHead(self, listNode):
    stack, h = [], listNode
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]
```

### 7.重建二叉树
说明：根据前序遍历和中序遍历重建二叉树，假设遍历结果中不包含重复的数字。
{% post_link LeetCode算法题整理（二叉树篇）Tree 105. Construct Binary Tree from Preorder and Inorder Traversal %}

### 9.用两个栈实现队列

{% post_link LeetCode算法题整理（设计篇）Design 232. Implement Queue using Stacks %}

### 9.1用两个队列实现栈

{% post_link LeetCode算法题整理（设计篇）Design 225. Implement Stack using Queues %}

