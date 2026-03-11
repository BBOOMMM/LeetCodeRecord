#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30204
#
# [1143] 最长公共子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] 表示 text1 的前 i 个和 text2 的前 j 个最长公共子序列长度
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len1][len2]
# @lc code=end



#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

