#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30204
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        dummy_head = dummy 
        
        p1 = dummy_head
        p2 = head
        p3 = head.next
        
        while p2 and p3:
            p1.next = p3
            p2.next = p3.next
            p3.next = p2
            
            p1 = p2
            if not p1.next or not p1.next.next:
                break
            p2 = p1.next
            p3 = p1.next.next
        
        return dummy_head.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

