#
# @lc app=leetcode.cn id=516 lang=python3
# @lcpr version=30204
#
# [516] 最长回文子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] 表示 s[i:j+1] 中的最长回文子序列长度
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n-1):
            # dp[i][i] = 1
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
        for k in range(2, n):
            for i in range(n):
                j = i + k
                if j >= n:
                    break
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2)
        # print(dp)
        # for l in dp:
            # print(l)
        return dp[0][n-1]
# @lc code=end



#
# @lcpr case=start
# "bbbab"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

