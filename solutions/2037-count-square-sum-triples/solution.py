class Solution:
    def countTriples(self, n: int) -> int:
        upper = n ** 2
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                s = i ** 2 + j ** 2
                if sqrt(s) <= n and sqrt(s) == sqrt(s) // 1:
                    count += 1

        return count
