#
# @lc app=leetcode.cn id=LCR 143 lang=python3
# @lcpr version=30204
#
# [LCR 143] 子结构判断
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
        self.ans = False
    
    def judge(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        
        re1 = self.judge(root1.left, root2.left)
        re2 = self.judge(root1.right, root2.right)
        
        return re1 and re2
    
    def preorderA(self, A, B):
        if self.ans:
            return
        
        if not A:
            return
        
        if A.val == B.val:
            re = self.judge(A, B)
            if re:
                self.ans = True
                return
        self.preorderA(A.left, B)
        self.preorderA(A.right, B)
            
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        # 先序遍历A，找到和B根节点相同的节点，遍历B比较
        if not A or not B:
            return False
        self.preorderA(A, B)
        return self.ans
# @lc code=end



#
# @lcpr case=start
# [1,7,5]\n[6,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,6,7,1,8]\n[6,1]\n
# @lcpr case=end

#

