#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找最后一段 严格升序段，记录终点
        if len(nums) <= 1:
            return nums
        up_end = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up_end = i
        print(up_end)
        if up_end == -1:
            # 全降序
            nums[:] = nums[::-1]
        else:
            if up_end == len(nums) - 1:
                nums[up_end-1], nums[up_end] = nums[up_end], nums[up_end-1]
            else:
                # up_end 不是最后，后面是一个降序段，取最小正好比 nums[up_end-1] 大的进行交换
                idx = None
                for j in range(len(nums)-1, up_end-1, -1):
                    if nums[j] > nums[up_end-1]:
                        idx = j
                        break
                nums[up_end-1], nums[idx] = nums[idx], nums[up_end-1]
                nums[up_end:] = sorted(nums[up_end:])
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#

