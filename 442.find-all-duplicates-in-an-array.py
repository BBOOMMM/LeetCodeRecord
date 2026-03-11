#
# @lc app=leetcode.cn id=442 lang=python3
# @lcpr version=30204
#
# [442] 数组中重复的数据
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 下表和数字进行哈希，把对应数字放到对应位置上，如果相等则下一位
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans
# @lc code=end



#
# @lcpr case=start
# [4,3,2,7,8,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

