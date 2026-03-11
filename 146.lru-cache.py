#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class DLinkedNode:
    def __init__(self, key=0, value=0, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        
        self.cache = {}  # value 存 node
        
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # 将该节点移动到双向链表头部
            node = self.cache[key]
            self.put_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 将该节点移动到双向链表头部
            node = self.cache[key]
            node.value = value
            self.put_to_head(node)
        else:
            new_node = DLinkedNode(key=key, value=value)
            self.cache[key] = new_node
            if self.size < self.capacity:
                self.size += 1
                # 在双向链表头部添加
                self.put_new_node_to_head(new_node)
            else:
                # 删除双向链表尾部节点和cache
                self.remove_last_node_and_cache()
                # 在双向链表头部添加
                self.put_new_node_to_head(new_node)
    
    def put_to_head(self, node):
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        
        head_next = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = head_next
        head_next.pre = node
    
    def put_new_node_to_head(self, node):
        head_next = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = head_next
        head_next.pre = node
    
    def remove_last_node_and_cache(self):
        last_node = self.tail.pre
        last_last_node = last_node.pre
        last_last_node.next = self.tail
        self.tail.pre = last_last_node
        
        key = last_node.key
        
        del self.cache[key]
        del last_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



