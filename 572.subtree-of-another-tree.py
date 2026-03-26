#
# @lc app=leetcode.cn id=572 lang=python3
# @lcpr version=30204
#
# [572] 另一棵树的子树
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
    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif root1 and not root2:
            return False
        if root1.val != root2.val:
            return False
        left_ans = self.check(root1.left, root2.left)
        right_ans = self.check(root1.right, root2.right)
        return left_ans and right_ans
    
    def dfs(self, root, subroot):
        if not root and not subroot:
            return True
        if not root:
            return False
        ans1 = self.check(root, subroot)
        ans2 = self.dfs(root.left, subroot)
        ans3 = self.dfs(root.right, subroot)
        return ans1 or ans2 or ans3
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#

