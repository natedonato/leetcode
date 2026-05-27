class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low = {}
        up = {}

        for i, c in enumerate(word):
            if c.isupper():
                if c.lower() not in up:
                    up[c.lower()] = i
            else:
                low[c] = i

        count = 0
        for c in low:

            if c in up and low[c] < up[c]:
                count += 1

        return count

