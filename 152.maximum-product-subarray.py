#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_val_dp = [float('-inf')] * n
        min_val_dp = [float('inf')] * n
        max_val_dp[0] = nums[0]
        min_val_dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                max_val_dp[i] = max(nums[i], nums[i]*max_val_dp[i-1])
                min_val_dp[i] = min(nums[i], nums[i]*min_val_dp[i-1])
            else:
                max_val_dp[i] = max(nums[i], nums[i]*min_val_dp[i-1])
                min_val_dp[i] = min(nums[i], nums[i]*max_val_dp[i-1])
        
        return max(max_val_dp)
# @lc code=end



#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#

