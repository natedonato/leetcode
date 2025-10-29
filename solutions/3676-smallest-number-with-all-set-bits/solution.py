class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 0
        while x < n:
            x = (x << 1) + 1
        return x
