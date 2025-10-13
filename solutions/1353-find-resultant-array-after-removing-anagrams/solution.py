class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        out = []
        prev = None
        for i in range(len(words)):
            w = "".join(sorted(words[i]))

            if w != prev:
                prev = w
                out.append(words[i])

        return out
