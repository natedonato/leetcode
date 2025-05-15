class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = -1
        out = []
        for i in range(len(words)):
            curr = groups[i]
            if curr != prev:
                out.append(words[i])
                prev = curr
        return out 
