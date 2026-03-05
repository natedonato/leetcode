class Solution:
    def minOperations(self, s: str) -> int:
        odd = 0
        even = 0

        for i, c in enumerate(s):
            # odd
            if (c == "0" and i % 2 == 1) or (c == "1" and i % 2 == 0):
                odd += 1
            
            if (c == "0" and i % 2 == 0) or (c == "1" and i % 2 == 1):
                even += 1

        return min(odd, even)


