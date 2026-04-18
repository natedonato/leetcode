class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = 0
        n1 = n

        while n > 0:
            m *= 10
            m += n % 10
            n //= 10

        return abs(m - n1)
