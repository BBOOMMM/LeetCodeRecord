#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30204
#
# [169] 多数元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        defend = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == defend:
                count += 1
            else:
                count -= 1
                if count < 0:
                    defend = nums[i]
                    count = 1
        
        return defend
# @lc code=end



#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#

