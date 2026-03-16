#
# @lc app=leetcode.cn id=97 lang=python3
# @lcpr version=30204
#
# [97] 交错字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(1, n1+1):
            if dp[i-1][0] and s1[i-1]==s3[i-1]:
                dp[i][0] = True
        for j in range(1, n2+1):
            if dp[0][j-1] and s2[j-1]==s3[j-1]:
                dp[0][j] = True
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # s1 的前 i 个， s2 的前 j 个
                # s1 i-1 , s2 j-1
                # s3 i + j - 1
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                elif s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[n1][n2]
# @lc code=end



#
# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbcbcac"\n
# @lcpr case=end

# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbbaccc"\n
# @lcpr case=end

# @lcpr case=start
# ""\n""\n""\n
# @lcpr case=end

#

