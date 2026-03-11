#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30204
#
# [94] 二叉树的中序遍历
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
        self.ans = []
    
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.ans.append(root.val)
        self.traverse(root.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.ans
        
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

