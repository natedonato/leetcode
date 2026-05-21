class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}

        for n in arr1:
            s = str(n)
            node = trie
            for c in s:
                if c not in node:
                    node[c] = {}
                node = node[c]

        best = 0
        for n in arr2:
            s = str(n)
            curr = 0
            node = trie
            for c in s:
                if c not in node:
                    break
                node = node[c]
                curr += 1
                best = max(best, curr)

        return best
