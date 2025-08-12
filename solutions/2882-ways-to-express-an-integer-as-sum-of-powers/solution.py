memo = {}

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        base_of_exponent = 1
        self.powers = []
        while base_of_exponent ** x <= n:
            self.powers.append(base_of_exponent ** x)
            base_of_exponent += 1
        self.x = x 
        return self.solve(n, 0) % (10 ** 9 + 7)

    def solve(self, n, i):
        if n < 0:
            return 0
        if n == 0:
            return 1

        key = (self.x, n, i)

        if key in memo:
            return memo[key]

        total = 0

        for index in range(i, len(self.powers)):
            total += self.solve(n - self.powers[index], index + 1)

        memo[key] = total
        return total

