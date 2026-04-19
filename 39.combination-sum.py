#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.path = []
        self.re = []
        self.cur_sum = 0
    
    def backtracking(self, candidates, index, target):
        if self.cur_sum == target:
            self.re.append(self.path[:])
            return 

        for i in range(index, len(candidates)):
            if self.cur_sum + candidates[i] > target:
                break 
            self.cur_sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, i, target)
            self.cur_sum -= candidates[i]
            self.path.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, 0, target)
        return self.re
# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

