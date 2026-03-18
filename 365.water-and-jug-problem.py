#
# @lc app=leetcode.cn id=365 lang=python3
# @lcpr version=30204
#
# [365] 水壶问题
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # 方法一：DFS（六种可能）
          # 把 X 壶的水灌进 Y 壶，直至灌满或倒空；
          # 把 Y 壶的水灌进 X 壶，直至灌满或倒空；
          # 把 X 壶灌满；
          # 把 Y 壶灌满；
          # 把 X 壶倒空；
          # 把 Y 壶倒空。
        # 方法二：数学
          # 每次操作只会让桶里的水 总量 增加 x，增加 y，减少 x，或者减少 y
          # 在题目所给的操作下，两个桶不可能同时有水且不满，操作的结果都至少有一个桶是空的或者满的；
          # 对一个不满的桶加水是没有意义的。因为如果另一个桶是空的，那么这个操作的结果等价于直接从初始状态给这个桶加满水；而如果另一个桶是满的，那么这个操作的结果等价于从初始状态分别给两个桶加满。
          # 把一个不满的桶里面的水倒掉是没有意义的。因为如果另一个桶是空的，那么这个操作的结果等价于回到初始状态；而如果另一个桶是满的，那么这个操作的结果等价于从初始状态直接给另一个桶倒满。
          # 从水总量考虑，ax + by = z
          #   贝祖定理告诉我们， ax + by = z 有解当且仅当 z 是 x,y 的最大公约数的倍数
        
        if target > x + y:
            return False
        gcd = math.gcd(x, y)
        if target % gcd == 0:
            return True
        return False


# @lc code=end



#
# @lcpr case=start
# 3\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n6\n5\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n3\n
# @lcpr case=end

#

