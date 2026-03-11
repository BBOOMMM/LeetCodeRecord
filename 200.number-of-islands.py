#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def traverse(self, grid, m, n, i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return 
        grid[i][j] = '2'
        self.traverse(grid, m, n, i-1, j)
        self.traverse(grid, m, n, i+1, j)
        self.traverse(grid, m, n, i, j-1)
        self.traverse(grid, m, n, i, j+1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_island += 1
                    self.traverse(grid, m, n, i, j)
        return num_island
# @lc code=end



#
# @lcpr case=start
# [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]\n
# @lcpr case=end

# @lcpr case=start
# [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]\n
# @lcpr case=end

#

