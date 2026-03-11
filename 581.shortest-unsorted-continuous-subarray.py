#
# @lc app=leetcode.cn id=581 lang=python3
# @lcpr version=30204
#
# [581] 最短无序连续子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # numsA, numsB, numsC
        # 左边需要从后往前确定
        left = -1
        min_val = float('inf')
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] < min_val:
                min_val = nums[i]
            elif nums[i] > min_val:
                left = i
        
        right = n
        max_val = float('-inf')
        for i in range(n):
            if nums[i] > max_val:
                max_val = nums[i]
            elif nums[i] < max_val:
                right = i
        
        if left == -1 and right == n:
            return 0
        elif left == -1:
            return right + 1
        elif right == n:
            return n - left
        return right - left + 1
# @lc code=end



#
# @lcpr case=start
# [2,6,4,8,10,9,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

