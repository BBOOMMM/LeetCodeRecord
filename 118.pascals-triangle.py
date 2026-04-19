#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        re = [[1],[1,1]]
        for _ in range(numRows-2):
            cur = [1]
            for i in range(len(re[-1])-1):
                num = re[-1][i] + re[-1][i+1]
                cur.append(num)
            cur.append(1)
            re.append(cur)
        return re
        
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

