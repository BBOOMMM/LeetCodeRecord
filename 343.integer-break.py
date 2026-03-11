#
# @lc app=leetcode.cn id=343 lang=python3
# @lcpr version=30204
#
# [343] 整数拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] 表示将整数 i 拆分成至少两个正整数的最大乘积
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

