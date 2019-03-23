### 60 n个骰子的点数

#### [AcWing传送门](https://www.acwing.com/problem/content/76/)

```
[[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]]
```

`dp[0][j]==1`表示第一个骰子和为`j+1`的次数为1，因为数组下标从0开始。

```python
def dice_probability(n, val=6):
    dp = [[0]*val*n for _ in range(n)]
    dp[0][:val] = [1] * val  # 初始化第一个骰子
    
    for i in range(n-1):  # 根据第i个骰子更新第i+1个骰子
        for j in range(i, len(dp[i+1])):
            # 第i+1个骰子和为j（实际为j+1，因为数组下标从0开始）的次数，等于第i个
            # 骰子j-1 ~ j-6次数的总和
            dp[i+1][j] = sum([dp[i][j-k] for k in range(1, val+1)])
            
    # 整理数据成为dict，key表示和，value表示出现的次数
    # count = {i+1: times for i, times in enumerate(dp[-1])}
    # 计算概率
    count = {i+1: round(float(times / (val**n)), 5)
             for i, times in enumerate(dp[-1]) if times!=0}
    return count
```

感觉用dict来表示更加明确，没有数组下标从0开始的混淆。按照AcWing中的返回写出一种解法。

```python
from collections import defaultdict
from itertools import repeat

def numberOfDice(self, n):
    last_p = defaultdict(int)
    last_p.update(dict(zip(range(1, 7), repeat(1))))
    for i in range(2, n+1):
        new_p = defaultdict(int)
        for j in range(i, i*6+1):
            new_p[j] = sum(last_p[j-k] for k in range(1, 7))
        # print(new_p)
        last_p = new_p
    return list(last_p.values())
```

### 61 扑克牌中的顺子

#### [牛客网传送门](https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/77/)

开始以为还要用个dict来映射值，后来发现直接传得卡牌的值。思想就是先排序，然后查joker的数量，看剩下牌的差值加起来能不能用已有的joker连起来。

```python
def IsContinuous(self, numbers):
    if not numbers:
        return False
    joker_count = numbers.count(0)
    left_cards = sorted(numbers)[joker_count:]
    need_joker = 0
    for i in range(len(left_cards)-1):
        if left_cards[i+1] == left_cards[i]:
            return False
        need_joker += (left_cards[i+1]-left_cards[i]-1)
    return need_joker <= joker_count
```

使用标准库，更加优雅，原理相同。

```python
from itertools import tee

def IsContinuous(self, numbers):
    if not numbers:
        return False
    joker_count = numbers.count(0)
    left_cards = sorted(numbers)[joker_count:]
    need_joker = 0
    c1, c2 = tee(left_cards)
    next(c2, None)
    for s, g in zip(c1, c2):
        if g == s:
            return False
        need_joker += g - 1 - s
    return need_joker <= joker_count
```



### 62 圆圈中最后剩下的数字

#### [牛客网传送门](https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
#### [AcWing传送门](https://www.acwing.com/problem/content/78/)

方法一：其实不需要环形链表，使用一个list足矣，每次将其旋转`rot`位，一开始想将要把第m个数旋转到list首部，然后再`pop(0)`，后来想到直接可以通过切片取出来，节省了`pop(0)`的O(n)复杂度。

```python
def LastRemaining_Solution(self, n, m):
    if n<=0 or m<=0:
        return -1
    seats = range(n)
    while seats:
        rot = (m-1) % len(seats)
        seats, last = seats[rot+1:] + seats[:rot], seats[rot]
    return last
```

方法二：书中的推导过程过于复杂，这里学到了一个稍微简单的推导过程。参考[约瑟夫环问题](https://blog.oldj.net/2010/05/27/joseph-ring/)。[我自己的拙见](https://darktiantian.github.io/%E7%BA%A6%E7%91%9F%E5%A4%AB%E7%8E%AF%E9%97%AE%E9%A2%98%EF%BC%88Josephus-problem%EF%BC%89/)。

```python
def LastRemaining_Solution(self, n, m):
    if n<=0 or m<=0:
        return -1
    last_num = 0
    for i in range(2, n+1):
        last_num = (last_num+m) % i
    return last_num
```

### 63 股票的最大利润

#### [LeetCode传送门](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

方法一：Brute Force.其实就是求最高峰点和前面最低谷点的差。

```python
def maxProfit(self, prices: List[int]) -> int:
    profit, min_buy = 0, float('inf')
    for p in prices:
        min_buy = min(min_buy, p)
        profit = max(profit, p-min_buy)
    return profit
```

方法二：标准的卡登算法。此题为53.连续数组最大和的变形，如果价格比之前小，则舍弃，否则一起计算连续子数组的和。

```python
def maxProfit(self, prices: List[int]) -> int:
    cur = sofar = 0
    for i in range(1, len(prices)):
        cur += prices[i] - prices[i-1]
        cur = max(0, cur)
        sofar = max(cur, sofar)
    return sofar
```

方法三：使用标准库的卡登算法。

```python
def maxProfit(self, prices: List[int]) -> int:
    from itertools import tee
    cur = profit = 0
    a, b = tee(prices)
    next(b, None)
    for before, today in zip(a, b):
        cur += today - before
        cur = max(0, cur)
        profit = max(profit, cur)
    return profit
```

