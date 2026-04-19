#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.path = []
        self.re = []
    
    def backtracking(self, nums, index):
        if len(self.path) <= len(nums):
            self.re.append(self.path[:])
        
        for i in range(index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.re
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

