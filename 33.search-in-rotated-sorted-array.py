#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = None
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[right]:
                if nums[mid] >= nums[left]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] <= nums[right]:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else: # 处于单增区间
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
        return -1
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

