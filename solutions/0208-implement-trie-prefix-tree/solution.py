class Trie:

    def __init__(self):
        self.trie = {"end": False}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {"end": False}
            node = node[c]

        node["end"] = True


    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return node["end"] == True

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
