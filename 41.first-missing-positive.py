#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # index 用来对应 1...n正整数
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                index = nums[i] - 1
                nums[index], nums[i] = nums[i], nums[index]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

