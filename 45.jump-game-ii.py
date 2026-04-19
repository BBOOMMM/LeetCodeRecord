#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        end = 0
        while end < len(nums)-1:
            max_dist = 0
            next_idx = -1
            for i in range(nums[end]+1):
                # 最远距离
                if end + i >= len(nums) - 1:
                    return count+1
                cur_dist = i + nums[end+i]
                if cur_dist > max_dist:
                    max_dist = cur_dist
                    next_idx = end + i 
            end = next_idx
            count += 1
        return count
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

