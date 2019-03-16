### 64 求1+2+···+n

#### [牛客网传送门](https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1?tpId=13&tqId=11200&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

这题对python不是很友好，感觉`and`也属于条件判断语句。`reduce``sum`之类的属于作弊行为，这里就不贴了。

```python
def Sum_Solution(self, n):
    return n and (n+self.Sum_Solution(n-1))
```

### 65 不用加减乘除做加法

#### [LeetCode传送门](https://leetcode.com/problems/sum-of-two-integers/description/)

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