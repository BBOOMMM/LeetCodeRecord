#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
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
    def flat(self, root):
        if not root:
            return None
        left_tree = root.left
        right_tree = root.right
        root.left = None 
        left_flat = self.flat(left_tree)
        right_flat = self.flat(right_tree)
        if not left_flat:
            root.right = right_flat
            return root
        cur = left_flat
        while cur.right:
            cur = cur.right
        cur.right = right_flat
        root.right = left_flat
        return root
        
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.flat(root)
# @lc code=end



#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

