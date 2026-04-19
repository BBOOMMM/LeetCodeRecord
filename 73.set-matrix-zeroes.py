#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        # 第一行是否有 0 
        first_row_has_zero = False
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break 
        
        # 第一列是否有 0
        first_col_has_zero = False
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break 
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 根据记录行置 0
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        
        # 根据记录列置 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

