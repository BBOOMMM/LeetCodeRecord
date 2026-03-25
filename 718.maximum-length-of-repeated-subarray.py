#
# @lc app=leetcode.cn id=718 lang=python3
# @lcpr version=30204
#
# [718] 最长重复子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] 表示以 nums1[i] 结尾和以 nums2[j] 结尾的最长公共子数组
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for j in range(n):
            # dp[0][j]
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
                ans = 1
        for i in range(m):
            # dp[i][0]
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                ans = 1
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans, dp[i][j])
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,2,1]\n[3,2,1,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n[0,0,0,0,0]\n
# @lcpr case=end

#

