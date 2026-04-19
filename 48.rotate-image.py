#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30204
#
# [48] 旋转图像
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        loops = n // 2
        for i in range(loops):
            start_row = i 
            start_col = i 
            side_length = n - i*2
            end_row = start_row + side_length - 1
            end_col = start_col + side_length - 1
            for j in range(side_length-1):
                num1 = matrix[start_row][start_col+j]
                num2 = matrix[start_row+j][end_col]
                num3 = matrix[end_row][end_col-j]
                num4 = matrix[end_row-j][start_col]
                
                matrix[start_row][start_col+j] = num4
                matrix[start_row+j][end_col] = num1 
                matrix[end_row][end_col-j] = num2
                matrix[end_row-j][start_col] = num3
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

