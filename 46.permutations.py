#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.re = []
        self.path = []
    
    def traverse(self, nums, used):
        if len(self.path) == len(nums):
            self.re.append(self.path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.traverse(nums, used)
            self.path.pop()
            used[i] = False
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.traverse(nums, used)
        return self.re
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

