class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = ""

        for word in words:
            score = 0
            for c in word:
                score += weights[ord(c) - ord("a")]

            score %= 26
            out += chr(ord("z") - score)

        return out
