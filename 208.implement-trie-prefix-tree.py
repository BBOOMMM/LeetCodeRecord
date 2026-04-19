#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30204
#
# [208] 实现 Trie (前缀树)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TreeNode:
    def __init__(self):
        self.childen = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        # 不能只是一个字典，因为如果有 cat 和 catt，就无法判断 cat 是一个完整单词还是前缀
        self.dummy = TreeNode()

    def insert(self, word: str) -> None:
        cur_node = self.dummy
        for ch in word:
            if ch in cur_node.childen:
                cur_node = cur_node.childen[ch]
            else:
                cur_node.childen[ch] = TreeNode()
                cur_node = cur_node.childen[ch]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        cur_node = self.dummy
        for ch in word:
            if ch in cur_node.childen:
                cur_node = cur_node.childen[ch]
            else:
                return False
        if cur_node.isEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.dummy
        for ch in prefix:
            if ch in cur_node.childen:
                cur_node = cur_node.childen[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end



