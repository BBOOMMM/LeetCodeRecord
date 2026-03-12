#
# @lc app=leetcode.cn id=491 lang=python3
# @lcpr version=30204
#
# [491] 非递减子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.ans =[]
        self.path = []
    
    def traverse(self, nums, startindex):
        if len(self.path) >= 2:
            self.ans.append(self.path[:])
        
        used = set()
        for i in range(startindex, len(nums)):
            if self.path and nums[i] < self.path[-1]:
                continue

            if nums[i] in used:
                continue
            
            used.add(nums[i])
            self.path.append(nums[i])
            self.traverse(nums, i+1)
            self.path.pop()
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.traverse(nums, 0)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,3,2,1]\n
# @lcpr case=end

#

