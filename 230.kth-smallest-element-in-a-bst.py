#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第 K 小的元素
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
        self.count = 0
        self.ans = None
        
    def midorder(self, root, k):
        if not root:
            return
        
        self.midorder(root.left, k)
        self.count += 1
        if self.count == k:
            self.ans = root.val
        self.midorder(root.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.midorder(root, k)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

