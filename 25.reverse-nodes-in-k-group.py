#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        
        group_pre = dummy
        cur_head = head 
        while group_pre:
            p = group_pre
            for _ in range(k):
                p = p.next 
                if not p:
                    return dummy.next 
            cur_tail = p 
            group_next = p.next 
            # 反转 cur_head 和 cur_tail 之间的节点
            pre = None 
            q = cur_head
            while q!=group_next:
                next_node = q.next
                q.next = pre 
                pre = q 
                q = next_node
            group_pre.next = cur_tail
            cur_head.next = group_next
            group_pre = cur_head
            cur_head = group_next
        
        return dummy.next

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

