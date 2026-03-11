#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.ans = []
        self.path = ''
    
    def traverse(self, leftnum, rightnum, n):
        if len(self.path) == 2*n:
            self.ans.append(self.path[:])
        
        if leftnum < n:
            self.path = self.path + '('
            leftnum += 1
            self.traverse(leftnum, rightnum, n)
            leftnum -= 1
            self.path = self.path[:-1]
        
        if leftnum > rightnum:
            self.path = self.path + ')'
            rightnum += 1
            self.traverse(leftnum, rightnum, n)
            rightnum -= 1
            self.path = self.path[:-1]
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.traverse(0,0,n)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

