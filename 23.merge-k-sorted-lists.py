#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
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
    def two_merge(self, head1, head2):
        dummy = ListNode()
        p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                p = p.next
                head1 = head1.next 
            else:
                p.next = head2
                p = p.next
                head2 = head2.next
        if head1:
            p.next = head1 
        if head2:
            p.next = head2 
        return dummy.next 
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            cur_list = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    head1 = lists[i]
                    head2 = lists[i+1]
                    new_head = self.two_merge(head1, head2)
                    cur_list.append(new_head)
                else:
                    head = lists[i]
                    cur_list.append(head)
            lists = cur_list
        
        return lists[0]
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

