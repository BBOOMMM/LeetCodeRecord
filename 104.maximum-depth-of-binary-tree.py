#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
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
    def getMaxDepth(self, root):
        if not root:
            return 0
        
        leftmaxdepth = self.getMaxDepth(root.left)
        rightmaxdepth = self.getMaxDepth(root.right)
        
        return 1 + max(leftmaxdepth, rightmaxdepth)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root)
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

