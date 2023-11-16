"""
Solution leetcode (dictionnaire de dictionnaire)
"""

class Trie:
    def __init__(self):
        self.nodes = dict()

    def insert(self, word: str) -> None:
        node = self.nodes
        for s in word:
            node[s] = node.get(s, dict())
            node = node[s]
        node['##'] = True

    def search(self, word: str) -> bool:
        node = self.nodes
        for s in word:
            node = node.get(s, None)
            if not node:
                return False
        return True if node.get('##', False) else False

    def startsWith(self, prefix: str) -> bool:
        node = self.nodes
        for s in prefix:
            node = node.get(s, None)
            if not node:
                return False
        return True