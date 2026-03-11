#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30204
#
# [543] 二叉树的直径
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
        self.ans = 0
    
    def max_length(self, root):
        if not root:
            return 0
        
        left_h = self.max_length(root.left)
        right_h = self.max_length(root.right)
        
        self.ans = max(self.ans, 1 + left_h + right_h)
        
        return 1 + max(left_h, right_h)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _ = self.max_length(root)
        return self.ans - 1
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

