#
# @lc app=leetcode.cn id=378 lang=python3
# @lcpr version=30204
#
# [378] 有序矩阵中第 K 小的元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countLessEqual(self, matrix, mid):
        m = len(matrix)
        n = len(matrix[0])
        i = m-1
        j = 0
        count = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        left = matrix[0][0]
        right = matrix[m-1][n-1]
        while left <= right:
            mid = (left + right) // 2
            if self.countLessEqual(matrix, mid) == k:
                right = mid - 1
                # 这里不能直接return mid，因为mid可能不在矩阵中，要找到最小的那个
            elif self.countLessEqual(matrix, mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

        j = 0
        
# @lc code=end



#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

