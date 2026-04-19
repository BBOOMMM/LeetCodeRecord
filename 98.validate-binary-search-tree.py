#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30204
#
# [98] 验证二叉搜索树
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
        self.pre = float('-inf')
        
    def midorder(self, root):
        if not root:
            return 
        
        self.midorder(root.left)
        if root.val <= self.pre:
            self.ans = False
        self.pre = root.val
        self.midorder(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.midorder(root)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

