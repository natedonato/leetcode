class Solution:
    def maxOperations(self, s: str) -> int:
        current_block = 0
        ops = 0
        for i in range(len(s)):
            c = s[i]
            if c == "1":
                current_block += 1
                if i + 1 < len(s) and s[i + 1] == "0":
                    ops += current_block

        return ops
