class Solution:
    def soupServings(self, n: int) -> float:
        if n > 10000:
            return float(1)
        self.cache = {}
        return self.solve(n,n)

    def solve(self, a, b):
        key = (a,b)
        if key in self.cache:
            return self.cache[(a,b)]
        elif a <= 0 and b <= 0:
            return (0.5)
        elif a <= 0:
            return (1)
        elif b <= 0:
            return (0)
        else:
            ans = 0.25 * self.solve(a-100, b) \
            + 0.25 * self.solve(a-75, b-25) \
            + 0.25 * self.solve(a-50, b-50) \
            + 0.25 * self.solve(a-25, b-75)
            self.cache[key] = ans
            return ans

