class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = 99999
        for n in nums:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10

            m = min(m, s)
        return m
