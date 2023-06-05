class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endofWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endofWord = True

    def search(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.endofWord

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True

obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
print(obj.insert('app'))
print(obj.search('app'))
