#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
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
    def Merge(self, node1, node2):
        # node1, node2已保证不可能为空
        p = node1
        q = node2
        dummy = ListNode(0)
        re = dummy
        while p and q:
            if p.val < q.val:
                re.next = p
                p = p.next 
            else:
                re.next = q 
                q = q.next 
            re = re.next
        if p:
            re.next = p
        elif q:
            re.next = q 
        return dummy.next
        
    def SplitMiddle(self, head):
        p = head
        q = head
        while q.next and q.next.next:
            p = p.next 
            q = q.next.next 
        node1 = head
        node2 = p.next 
        p.next = None
        return node1, node2
    
    def MergeSort(self, node):
        # 基础情况，只有一个节点
        if not node.next:
            return node
        # 找中间节点分割
        node1, node2 = self.SplitMiddle(node)
        sorted_node1 = self.MergeSort(node1)
        sorted_node2 = self.MergeSort(node2)
        ans = self.Merge(sorted_node1, sorted_node2)
        return ans
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序 O(nlogn)
        if not head:
            return head
        return self.MergeSort(head)
# @lc code=end



#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

