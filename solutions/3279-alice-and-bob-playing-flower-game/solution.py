class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        total = 0
        total += self.evencount(n) * self.oddcount(m)
        total += self.oddcount(n) * self.evencount(m)

        return total

    def evencount(self , i):
        return i // 2

    def oddcount(self, i):
        if i % 2 != 0:
            i += 1
        return i // 2
