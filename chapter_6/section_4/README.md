### 60 n个骰子的点数

#### 404.

关于此题的实现，并没有找到特别pythonic的解法，大多都是直接从c++'翻译'过来的，参考[leetcode之n个骰子的点数，python版本](https://blog.csdn.net/leokingszx/article/details/80794407)，在此之上做了一些优化。dp表示所有骰子的结果集合，dp中的元素表示该骰子所有的次数集合，如下n=2后，dp为

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

感觉用dict来表示更加明确，没有数组下标从0开始的混淆。

```python
def dice_probability_dict(n, val=6):
    from collections import defaultdict
    dp = defaultdict(int)
    dp.update({k: 1 for k in range(1, val+1)})  # 初始化第一个骰子
    for i in range(n-1):  # 根据第i个骰子更新第i+1个骰子
        new_dp = defaultdict(int)
        for j in range(n*(i+1), val*n+1):  # n个骰子最小值为n*(i+1)，最大值为val*n  
            # 第i+1个骰子和为j（实际为j+1，因为数组下标从0开始）的次数，等于第i个
            # 骰子j-1 ~ j-6次数的总和
            new_dp[j] = sum(dp[j-k] for k in range(1, val+1))
        dp = new_dp

    # 这时的dp就是得到我们想要的了，只不过值为出现的次数，我们算一下概率
    count = {k: round(float(times / (val**n)), 5)
             for k, times in dp.items()}
    return count
```

### 61 扑克牌中的顺子

#### [牛客网传送门](https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

开始以为还要用个dict来映射值，后来发现直接传得卡牌的值。思想就是先排序，然后查joker的数量，看剩下牌的差值加起来能不能用已有的joker连起来。

```python
def IsContinuous(self, numbers):
    # poker = {k: k for k in range(2, 11)}
    # poker.update({'A': 1, 'J': 11, 'Q': 12, 'K': 13, '0': 0})
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

### 62 圆圈中最后剩下的数字

#### [牛客网传送门](https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)

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
    ans, min_buy = 0, float('inf')
    for price in prices:
        if price < min_buy:
            min_buy = price
        elif price-min_buy > ans:
            ans = price - min_buy
    return ans
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

