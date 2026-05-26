class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()

        for c in word:
            s.add(c)

        count = 0
        for c in s:
            if c.upper() in s and c.lower() in s:
                count += 1

        return count // 2
