#
# @lc app=leetcode.cn id=842 lang=python3
# @lcpr version=30204
#
# [842] 将数组拆分成斐波那契序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        
    def traverse(self, num, startindex):
        if startindex == len(num) and len(self.path) >= 3:
            self.ans = self.path[:]
            return
        
        for i in range(startindex, len(num)):
            if num[startindex] == '0' and i > startindex:
                break
            
            cur_num = int(num[startindex:i+1])
            if cur_num > 2**31 - 1:
                break
            
            if len(self.path) >= 2 and cur_num != self.path[-1] + self.path[-2]:
                continue
            
            self.path.append(cur_num)
            self.traverse(num, i+1)
            self.path.pop()
    
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.traverse(num, 0)
        return self.ans
        
# @lc code=end



#
# @lcpr case=start
# "1101111"\n
# @lcpr case=end

# @lcpr case=start
# "112358130"\n
# @lcpr case=end

# @lcpr case=start
# "0123"\n
# @lcpr case=end

#

