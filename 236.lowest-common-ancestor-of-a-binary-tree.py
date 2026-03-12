#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, root, p, q):
        if not root:
            return None
        
        left_ans = self.postorder(root.left, p, q)
        right_ans = self.postorder(root.right, p, q)
        
        if left_ans and right_ans:
            return root
        
        if root==p or root==q:
            return root
        
        if left_ans:
            return left_ans
        
        if right_ans:
            return right_ans
        
        return None
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.postorder(root, p, q)
# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

