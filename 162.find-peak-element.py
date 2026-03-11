#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30204
#
# [162] 寻找峰值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] > nums[mid-1] and mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == 0 and mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == len(nums)-1 and mid > 0 and nums[mid] > nums[mid-1]:
                return mid
            elif mid > 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid + 1
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

