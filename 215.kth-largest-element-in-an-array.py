#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def quickselect(self, nums, target_index, high, low):
        if high < low:
            return 
        pivot = nums[high]
        i = low
        j = high - 1
        # 越界处理
        while i <= j:
            while nums[i] <= pivot and i <= high-1:
                i += 1
            while nums[j] > pivot and j >= low:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        # # assert i == j + 1
        # [low, i-1] 为小于等于 pivot, [i, high-1] 为大于 pivot
        nums[i], nums[high] = nums[high], nums[i]
        # 交换后，[low, i] 为小于等于 pivot, [i+1, high] 为大于 pivot
        # if target_index == i:
        #     return nums[i]
        # elif target_index < i:
        #     return self.quickselect(nums, target_index, i-1, low)
        # 必须特别处理等于情况，不然会超时，划分枢纽在中间最佳
        if target_index <= i:
            p = i
            while nums[p] == pivot and p >= low: # 有点重复耗时
                p -= 1
            # [p+1, i] 为等于 pivot
            if target_index >= p+1:
                return pivot
            return self.quickselect(nums, target_index, p, low)
        else:
            return self.quickselect(nums, target_index, high, i+1)
        
    
    def quickselectimprove(self, nums, target_index, high, low):
        if high < low:
            return 
        pivot = nums[high]
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
        # # assert i == j + 1
        nums[i], nums[high] = pivot, nums[i]
        # [low, i-1] 为小于等于 pivot, [i, high] 为大于等于 pivot, nums[i] 确定为 pivot
        if target_index == i:
            return nums[i]
        elif target_index < i:
            return self.quickselectimprove(nums, target_index, i-1, low)
        else:
            return self.quickselectimprove(nums, target_index, high, i+1)
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第 k 大等于第 target 小
        target_index = len(nums) - k
        return self.quickselectimprove(nums, target_index, len(nums)-1, 0)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

