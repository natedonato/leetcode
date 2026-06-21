class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        out = 0
        for c in costs:
            if c <= coins:
                coins -= c
                out += 1

        return out
