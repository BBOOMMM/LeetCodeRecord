#
# @lc app=leetcode.cn id=110 lang=python3
# @lcpr version=30204
#
# [110] 平衡二叉树
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
        self.ans = True
    
    def postorder(self, root):
        if not self.ans:
            return 0
        
        if not root:
            return 0
        
        left_height = self.postorder(root.left)
        right_height = self.postorder(root.right)
        
        if abs(left_height - right_height) > 1:
            self.ans = False
        
        return max(left_height, right_height) + 1 
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.postorder(root)
        return self.ans

# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

