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