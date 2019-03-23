### 64 求1+2+···+n

#### [牛客网传送门](https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1?tpId=13&tqId=11200&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/80/)

这题对python不是很友好，感觉`and`也属于条件判断语句。`reduce``sum`之类的属于作弊行为，这里就不贴了。

```python
def Sum_Solution(self, n):
    return n and (n+self.Sum_Solution(n-1))
```

### 65 不用加减乘除做加法

#### [LeetCode传送门](https://leetcode.com/problems/sum-of-two-integers/description/)

此题由于Python中的int没有长度限制，在负数出现的情况，会导致结果与预期不同。详情见[Python负数位运算](https://darktiantian.github.io/371-Sum-of-Two-Integers-Python/)

```python
def getSum(self, a, b):
    # 32 bits integer max
    MAX = 0x7FFFFFFF  # 2**31-1
    # 32 bits interger min  
    MIN = 0x80000000  # -2**31
    # mask to get last 32 bits
    mask = 0xFFFFFFFF  # 2*32-1
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)
```

或者可以将其转成32位整数。

```python
import numpy as np

class Solution(object):
    def getSum(self, a, b):
        while b != 0:
            a, b = np.int32(a ^ b), np.int32((a & b) << 1)
        return int(a)
```

### 66 构建乘积数组

#### [牛客网传送门](https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=11204&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

#### [AcWing传送门](https://www.acwing.com/problem/content/82/)

思路：不能使用除法。如书中所说，以i为分割点，将B拆成C，D两部分，左边是`A[0] x A[1] x...x A[i-1]`右边则为`A[i+1] x ...x A[n-1]` ，C[i] = C[i-1] * A[i-1]

使用`accumulate`，牛客网居然不能AC，老是说我语法错误或数组越界？AcWing是可以的。我在自己的testcase中使用随机生成的方式验证了是可以的。

```python
def multiply(self, A):
    from itertools import accumulate
    from operator import mul
    C = [1] # 第一个元素相当于没有
    C += accumulate(A[:-1], mul)    # `+=`支持右边生成器，`+`不支持
    D = [1]
    D += accumulate(A[:0:-1], mul)
    D.reverse()
    return [C[i] * D[i] for i in range(len(A))]
```
不使用标准库的方法。

```python
def multiply(self, A):
    C = [1] # 第一个元素相当于没有
    for i in range(len(A)-1):
        C.append(C[-1] * A[i])
    D = [1]
    for j in range(len(A)-1, 0, -1):
        D.append(D[-1] * A[j])
    D.reverse()
    return [C[i] * D[i] for i in range(len(A))]
```