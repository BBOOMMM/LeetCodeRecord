#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
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
        self.ans = float('-inf')
    
    def post_order(self, root):
        if not root:
            return 0, 0
        
        left_left_max, left_right_max = self.post_order(root.left)
        right_left_max, right_right_max = self.post_order(root.right)
        num1 = left_left_max + root.val
        num2 = left_right_max + root.val
        num3 = right_left_max + root.val
        num4 = right_right_max + root.val
        num5 = max(num1,num2) - root.val + max(num3, num4)
        self.ans = max(self.ans, num1, num2, num3, num4, num5, root.val)
        return max(num1,num2,root.val), max(num3, num4, root.val)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.post_order(root)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#

