#
# @lc app=leetcode.cn id=912 lang=python3
# @lcpr version=30204
#
# [912] 排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import numpy as np

class Solution:
    def quickSort(self, nums, low, high):
        if low >= high:
            return
        # pivot = nums[high]
        idx = np.random.randint(low=low, high=high)
        pivot = nums[idx]
        nums[idx], nums[high] = nums[high], nums[idx]
        i = low - 1
        j = high
        while i < j:
            i += 1
            while nums[i] < pivot and i <= high:
                i += 1
            j -= 1
            while nums[j] > pivot and j >= low:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        # [low, i-1] 小于等于 pivot，[i, high] 小于等于 pivot
        nums[i], nums[high] = nums[high], nums[i]
        
        self.quickSort(nums, low, i-1)
        self.quickSort(nums, i+1, high)
        
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
# @lc code=end



#
# @lcpr case=start
# [5,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,2,0,0]\n
# @lcpr case=end

#

