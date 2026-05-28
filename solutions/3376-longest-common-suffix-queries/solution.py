class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = { "idx": 0}

        for i, word in enumerate(wordsContainer):
            if len(word) < len(wordsContainer[trie["idx"]]):
                trie["idx"] = i

            node = trie
            for c in reversed(word):
                if c not in node:
                    node[c] = {"idx": i}
                    node = node[c]
                else:
                    node = node[c]
                    if len(word) < len(wordsContainer[node["idx"]]):
                        node["idx"] = i
        
        out = []

        for word in wordsQuery:
            node = trie
            for c in reversed(word):
                if c not in node:
                    break
                node = node[c]

            out.append(node["idx"])

        return out
