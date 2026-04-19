#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = rows - 1
        while left <= right:
            mid = (left+right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        selected_row_idx = right 
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left+right) // 2
            if matrix[selected_row_idx][mid] == target:
                return True
            elif matrix[selected_row_idx][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

