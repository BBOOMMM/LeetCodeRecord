#
# @lc app=leetcode.cn id=112 lang=python3
# @lcpr version=30204
#
# [112] 路径总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = False
        self.cur = 0
    
    def dfs(self, node, target):
        if not node:
            return
        
        if self.ans:
            return
        
        self.cur += node.val
        if self.cur == target and not node.left and not node.right:
            self.ans = True
            return
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        self.cur -= node.val
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.dfs(root, targetSum)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

