class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 1
        while i < n:
            i *= 4
        return n % i == 0 and n > 0
