#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30204
#
# [72] 编辑距离
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] 表示前 word1 前 i 个和 word2 前 j 个相等需要的操作数
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[len1][len2]
# @lc code=end



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

