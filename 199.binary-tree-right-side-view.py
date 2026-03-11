#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30204
#
# [199] 二叉树的右视图
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

import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # queue = [root]
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            n = len(queue)
            # print(queue)
            # for node in queue:
            #     print(node.val, end=' ')
            #     print()
            for i in range(n):
                if i == n-1:
                    ans.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.popleft()
        return ans

                    
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

