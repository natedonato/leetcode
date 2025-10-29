class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        c = 1
        while x < n:
            x += 2 **c
            c += 1
        return x
