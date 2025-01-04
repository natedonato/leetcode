class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            val = ord(c) - ord("a")
            if first[val] == -1:
                first[val] = i
            else:
                last[val] = i
        count = 0

        for i in range(26):
            if last[i] != -1:
                between = set()
                for j in range (first[i] + 1, last[i]):
                    between.add(s[j])
                
                count += len(between)

        return count
