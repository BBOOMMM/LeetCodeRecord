#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def find(self, board, i, j, m, n, idx, word):
        # 走过的一定不能重复走！需要回溯！
        ans = False
        def dfs(board, i, j, m, n, idx, word):
            nonlocal ans
            if ans:
                return
            if idx >= len(word):
                ans = True
                return
            if i<0 or i>=m or j<0 or j>=n:
                return
            if board[i][j] == '#':
                return 
            if not word[idx]==board[i][j]:
                return 
            
            board[i][j] = '#'
            dfs(board, i+1, j, m, n, idx+1, word)
            dfs(board, i, j+1, m, n, idx+1, word)
            dfs(board, i-1, j, m, n, idx+1, word)
            dfs(board, i, j-1, m, n, idx+1, word)
            board[i][j] = word[idx]
        
        dfs(board, i, j, m, n, idx, word)
        return ans
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.find(board, i, j, m, n, 0, word):
                        return True
        return False
# @lc code=end



#
# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"ABCB"\n
# @lcpr case=end

#

