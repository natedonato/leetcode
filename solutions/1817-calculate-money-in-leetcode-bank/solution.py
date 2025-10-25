class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        mon = 0
        prev = 0

        for i in range(n):
            if i % 7 == 0:
                mon += 1
                prev = mon
            total += prev
            prev += 1

        return total
