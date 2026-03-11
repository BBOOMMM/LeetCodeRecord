#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.ans = []
    
    def traverse(self, matrix, top, bottom, left, right):
        if top > bottom or left > right:
            return
        if top==bottom: # 一行
            for j in range(left, right+1):
                self.ans.append(matrix[top][j])
            return
        if left==right: # 一列
            for i in range(top, bottom+1):
                self.ans.append(matrix[i][left])
            return
        

        for j in range(left, right):
            self.ans.append(matrix[top][j])
        for i in range(top, bottom):
            self.ans.append(matrix[i][right])
        top += 1
        for j in range(right, left, -1):
            self.ans.append(matrix[bottom][j])
        right -= 1
        for i in range(bottom, top-1, -1):
            self.ans.append(matrix[i][left])
        bottom -= 1
        left += 1
        
        self.traverse(matrix, top, bottom, left, right)
    
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0]) - 1
        
        self.traverse(matrix, top, bottom, left, right)
        
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

