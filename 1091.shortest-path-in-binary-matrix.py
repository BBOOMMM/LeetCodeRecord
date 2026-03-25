#
# @lc app=leetcode.cn id=1091 lang=python3
# @lcpr version=30204
#
# [1091] 二进制矩阵中的最短路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 无权最短路径，bfs
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        # dist[i][j] 表示 i, j 到 0, 0 的距离, 正好代表 visit
        # dist = [[float('inf')] * n for _ in range(n)]
        # dist[0][0] = 1
        visited = [[False] * n for _ in range(n)]
        floor = 1
        q = deque([(0,0)])
        # 必须在入队时visited就标记为True!!!不然可能重复入队，如果两个节点都能到达下一个，会导致重复入队
        visited[0][0] = True
        while q:
            size_q = len(q)
            for _ in range(size_q):
                cur_i, cur_j = q.popleft()
                if cur_i == n-1 and cur_j == n-1:
                    return floor
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx==0 and dy==0:
                            continue
                        next_i = cur_i + dx
                        next_j = cur_j + dy
                        if 0<=next_i<n and 0<=next_j<n and (visited[next_i][next_j]==False) and (grid[next_i][next_j]==0):
                            visited[next_i][next_j] = True
                            q.append((next_i, next_j))
            floor+=1
        return -1
# @lc code=end



#
# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#

