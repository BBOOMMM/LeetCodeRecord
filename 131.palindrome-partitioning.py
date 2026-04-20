#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.path = []
        self.re = []
    
    def backtracking(self, s, idx):
        if idx == len(s):
            self.re.append(self.path[:])
            return 
        
        for i in range(idx, len(s)):
            # 分割点
            sub_str = s[idx : i+1]
            if sub_str == sub_str[::-1]:
                self.path.append(sub_str)
                self.backtracking(s, i+1)
                self.path.pop()
    
    
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.re
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

